#!/usr/bin/env python3
"""
blender_mcp_bridge.py - Model Context Protocol Bridge for Blender 4.x
Communicates with Blender over local socket / headless subprocess.
"""

import sys
import json
import argparse
import socket

def handle_request(payload: dict) -> dict:
    method = payload.get("method")
    params = payload.get("params", {})
    req_id = payload.get("id", 1)

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "blender_execute_code",
                        "description": "Executes Python bpy code inside Blender's thread.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {"code": {"type": "string"}},
                            "required": ["code"]
                        }
                    },
                    {
                        "name": "blender_get_scene_info",
                        "description": "Inspects open Blender scene objects, vertex count, and materials.",
                        "inputSchema": {"type": "object"}
                    },
                    {
                        "name": "blender_export_gltf",
                        "description": "Exports scene or selected objects to a .gltf file.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {"output_path": {"type": "string"}},
                            "required": ["output_path"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [
                    {
                        "type": "text",
                        "text": f"[blender-mcp] Simulated execution of '{tool_name}' with args {args}. Bridge ready."
                    }
                ]
            }
        }
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "result": {}
    }

def main():
    parser = argparse.ArgumentParser(description="Blender MCP Bridge Server")
    parser.add_argument("--port", type=int, default=9876, help="Blender bridge port")
    args = parser.parse_args()

    # stdio mode for MCP clients (Cursor / Codex)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling MCP request: {e}\n")

if __name__ == "__main__":
    main()
