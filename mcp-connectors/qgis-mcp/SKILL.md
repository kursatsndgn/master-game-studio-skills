---
name: qgis-mcp
description: Model Context Protocol (MCP) bridge for QGIS Desktop (OSGeo). Enables automated DEM elevation harvesting, 16-bit heightmap generation, slope/aspect splatmask calculations, vector GIS feature export (roads, rivers), and PyQGIS script execution.
---

# QGIS MCP Connector Skill

The **QGIS MCP Connector** connects AI agents to a live or headless QGIS environment using the open-source `qgis-mcp` architecture (FastMCP stdio bridge to local QGIS TCP socket on port 9877).

---

## 1. Architecture & Protocol

```mermaid
flowchart LR
    Agent["AI Agent (Codex / Cursor / Claude)"] <-->|MCP JSON-RPC (stdio)| Bridge["qgis_mcp_bridge.py"]
    Bridge <-->|TCP Socket (Port 9877)| Plugin["QGIS Desktop (QGIS MCP Plugin)"]
    Plugin <--> QGISEngine["QGIS Processing Core (GDAL, GRASS, PyQGIS)"]
```

---

## 2. Standard MCP Tools Exposed

### `qgis_export_heightmap`
Converts a 32-bit float DEM (GeoTIFF) into a normalized 16-bit Grayscale PNG/RAW heightmap formatted specifically for Unreal Landscape, Godot Terrain3D, or Unity Terrain.
- **Input:**
  ```json
  {
    "layer_name": "DEM_Alps_Sector4",
    "output_format": "PNG_16BIT",
    "target_resolution": [2017, 2017],
    "output_path": "terrain/heightmap_16bit.png"
  }
  ```
- **Output:**
  ```json
  {
    "status": "success",
    "file_path": "terrain/heightmap_16bit.png",
    "min_elevation_meters": 412.0,
    "max_elevation_meters": 2840.5
  }
  ```

### `qgis_calculate_slope_mask`
Generates a binary or grayscale splatmap mask representing terrain slope angles (e.g. slopes > 30 degrees for cliff rock textures).

### `qgis_export_vector_splines`
Filters OpenStreetMap (OSM) or custom road/river layers and exports them as GeoJSON coordinates ready for game-engine Bézier spline generation.

### `qgis_run_pyqgis`
Executes an arbitrary PyQGIS script directly inside the active QGIS Desktop canvas.

---

## 3. QGIS Plugin Setup (100% Free & Open-Source)

1. Open **QGIS Desktop** (Free download from [qgis.org](https://qgis.org)).
2. Go to **Plugins > Manage and Install Plugins**.
3. Search for **QGIS MCP** and click **Install Plugin**.
4. Click the **QGIS MCP** toolbar icon to start the local socket listener on port `9877`.
5. Your AI assistant will now automatically discover and manipulate active GIS layers.
