---
name: godot-mcp
description: Model Context Protocol (MCP) bridge for Godot 4. Enables SceneTree queries, node creation, GDScript execution, Resource serialization, and debug console inspection over TCP/WebSocket.
---

# Godot 4 MCP Connector Skill

The **Godot 4 MCP Connector** links AI agents directly to the Godot 4 Editor and running game instances via an asynchronous TCP/WebSocket bridge implemented as a Godot `EditorPlugin`.

---

## 1. Architecture & Protocol

```mermaid
flowchart LR
    Agent["AI Agent (Codex / Cursor / Claude)"] <-->|MCP JSON-RPC| Server["godot_mcp_bridge.py"]
    Server <-->|TCP / WebSocket (Port 9080)| Plugin["Godot 4 EditorPlugin\n(addons/godot_mcp/)"]
    Plugin <--> GodotTree["Godot 4 SceneTree & ResourceFileSystem"]
```

The plugin utilizes `EditorInterface` to ensure that node additions and property modifications register with the Godot Undo/Redo history stack and show immediate visual feedback in the 2D/3D viewports.

---

## 2. Standard MCP Tools Exposed

### `godot_get_scene_tree`
Queries the open scene's node tree hierarchy.
- **Input:**
  ```json
  {
    "filter_type": "Node3D",
    "include_groups": true
  }
  ```
- **Output:**
  ```json
  {
    "root_node": "LevelMain",
    "nodes": [
      {
        "name": "DirectionalLight3D",
        "type": "DirectionalLight3D",
        "path": "/root/LevelMain/DirectionalLight3D"
      },
      {
        "name": "Player",
        "type": "CharacterBody3D",
        "path": "/root/LevelMain/Player"
      }
    ]
  }
  ```

### `godot_instantiate_scene`
Instantiates a packed scene (`.tscn` or imported `.glb`) into the active scene tree.

### `godot_run_gdscript`
Evaluates a GDScript snippet dynamically inside the editor context.

### `godot_scan_filesystem`
Signals the Godot FileSystem dock to scan for external file changes and reimport modified resources.

---

## 3. Usage

```bash
python mcp-connectors/godot-mcp/godot_mcp_bridge.py --port 9080
```
