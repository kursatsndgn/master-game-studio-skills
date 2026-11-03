# Engine MCP Connectors (`mcp-connectors/`)
# Model Context Protocol Bridges for Blender, Godot, Unity & Unreal Engine 5

This directory contains production-ready Model Context Protocol (MCP) skills and bridge servers allowing AI coding agents (Codex, Cursor, Claude Code) to interact directly with live game engines and 3D DCC tools.

---

## 🏛️ Connector Architecture & Port Allocation

```mermaid
flowchart TD
    Agent["AI Agent (Codex / Cursor / Claude)"] --> Router["MCP Client (mcp.json)"]
    
    Router -->|JSON-RPC / stdio (Port 9876)| BlenderMCP["blender-mcp\n(Blender 4.x / bpy)"]
    Router -->|JSON-RPC / TCP (Port 9080)| GodotMCP["godot-mcp\n(Godot 4 EditorPlugin)"]
    Router -->|JSON-RPC / WS (Port 8080)| UnityMCP["unity-mcp\n(Unity EditorWindow)"]
    Router -->|JSON-RPC / HTTP (Port 30010)| UnrealMCP["unreal-mcp\n(UE5 Web Remote Control)"]
```

| Connector | Target Environment | Default Port / Protocol | Primary Capabilities |
|---|---|---|---|
| **`blender-mcp`** | Blender 4.x | `9876` (IPC / stdio) | Procedural 3D modeling, UV unwrapping, PBR shaders, viewport render, glTF export |
| **`godot-mcp`** | Godot 4.x | `9080` (WebSocket / TCP) | SceneTree inspection, node instancing, GDScript execution, FileSystem re-import |
| **`unity-mcp`** | Unity 2022+ / Unity 6 | `8080` (WebSocket / HTTP) | GameObject hierarchy, Prefab placement, AssetDatabase refresh, Playmode testing |
| **`unreal-mcp`** | Unreal Engine 5.x | `30010` (Web Remote Control) | Python Remote Execution, Level Actor spawn, Nanite/Lumen configuration |

---

## 🚀 Quick Activation

1. **In Cursor:** The `.cursor/mcp.json` file is pre-configured and automatically recognized by Cursor Composer.
2. **In Claude Desktop:** Point your `claude_desktop_config.json` to the root `mcp.json`.
3. **In Codex / CLI:** Launch individual bridges directly:
   ```bash
   python mcp-connectors/blender-mcp/blender_mcp_bridge.py
   python mcp-connectors/godot-mcp/godot_mcp_bridge.py
   python mcp-connectors/unity-mcp/unity_mcp_bridge.py
   python mcp-connectors/unreal-mcp/unreal_mcp_bridge.py
   ```
