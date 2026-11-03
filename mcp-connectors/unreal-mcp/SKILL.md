---
name: unreal-mcp
description: Model Context Protocol (MCP) bridge for Unreal Engine 5. Integrates with UE5 Python Remote Execution and Web Remote Control to inspect levels, spawn Actors, configure Nanite/Lumen, and manage Blueprints.
---

# Unreal Engine 5 MCP Connector Skill

The **Unreal Engine 5 MCP Connector** provides deep integration with the UE5 Editor environment using the built-in **Python Remote Execution** protocol and the **Web Remote Control** subsystem.

---

## 1. Architecture & Protocol

```mermaid
flowchart LR
    Agent["AI Agent (Codex / Cursor / Claude)"] <-->|MCP JSON-RPC| Server["unreal_mcp_bridge.py"]
    Server <-->|Remote Python / Web Remote Control (HTTP: 30010)| UE5["Unreal Engine 5 Editor\n(Editor Subsystems)"]
    UE5 <--> UELandscape["Level, Actors, Nanite/Lumen, Asset Registry"]
```

The bridge interacts with the `unreal` Python module inside the Unreal Editor, providing access to `unreal.EditorLevelLibrary`, `unreal.EditorAssetLibrary`, and `unreal.Subsystem`.

---

## 2. Standard MCP Tools Exposed

### `unreal_execute_python`
Executes Python scripts inside the live Unreal Editor context.
- **Input:**
  ```json
  {
    "script": "import unreal\nactors = unreal.EditorLevelLibrary.get_all_level_actors()\nprint(f'Total actors: {len(actors)}')"
  }
  ```
- **Output:**
  ```json
  {
    "status": "success",
    "output": "Total actors: 142"
  }
  ```

### `unreal_get_actors_in_level`
Returns all actors in the currently loaded world with class and transform data.

### `unreal_spawn_actor`
Spawns an Actor, Blueprint instance, or StaticMesh in the persistent level with optional Nanite toggle.

### `unreal_query_asset_registry`
Searches the Unreal Asset Registry for assets matching paths, classes, or metadata tags.

---

## 3. Usage

```bash
python mcp-connectors/unreal-mcp/unreal_mcp_bridge.py --port 30010
```
