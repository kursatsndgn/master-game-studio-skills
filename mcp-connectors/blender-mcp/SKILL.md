---
name: blender-mcp
description: Model Context Protocol (MCP) bridge for Blender 4.x. Enables real-time scene inspection, procedural mesh generation, modifier stacks, UV unwrapping, material nodes, and glTF exports over JSON-RPC.
---

# Blender MCP Connector Skill

The **Blender MCP Connector** links AI agents directly to a live or headless instance of Blender 4.x.

---

## 1. Architecture & Protocol

```mermaid
flowchart LR
    Agent["AI Agent (Codex / Cursor / Claude)"] <-->|MCP JSON-RPC (stdio)| Bridge["blender_mcp_bridge.py"]
    Bridge <-->|IPC / Socket (Port 9876)| BlenderAddon["Blender 4.x (bpy runtime)"]
    BlenderAddon <--> LiveScene["Active 3D Scene & Shader Nodes"]
```

The bridge operates in two modes:
1. **Interactive Add-on Mode:** Hooks into Blender's timer loop (`bpy.app.timers`), allowing non-blocking agent commands while the artist works in the GUI.
2. **Headless Microservice Mode:** Launches background Blender (`blender -b`) accepting JSON-RPC commands for automated asset pipelines.

---

## 2. Standard MCP Tools Exposed

### `blender_execute_code`
Executes Python code directly inside Blender's `bpy` thread.
- **Input:**
  ```json
  {
    "code": "import bpy\nbpy.ops.mesh.primitive_cylinder_add(radius=1.0, depth=2.0)"
  }
  ```
- **Output:**
  ```json
  {
    "status": "success",
    "stdout": "Created Cylinder at (0.0, 0.0, 0.0)"
  }
  ```

### `blender_get_scene_info`
Returns object names, polycounts, materials, and active selections.

### `blender_export_gltf`
Exports selected objects or the entire scene to glTF 2.0 with applied modifiers.

---

## 3. Usage

Run the standalone stdio MCP server:
```bash
python mcp-connectors/blender-mcp/blender_mcp_bridge.py --port 9876
```
