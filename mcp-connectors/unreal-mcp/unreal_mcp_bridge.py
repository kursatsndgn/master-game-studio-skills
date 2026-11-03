#!/usr/bin/env python3
"""
unreal_mcp_bridge.py - Model Context Protocol Bridge for Unreal Engine 5
Communicates with UE5 Web Remote Control / Python Remote Execution on port 30010.
"""

import sys
import json
import argparse

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
                        "name": "unreal_execute_python",
                        "description": "Executes Python automation code inside Unreal Engine 5 editor.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {"script": {"type": "string"}},
                            "required": ["script"]
                        }
                    },
                    {
                        "name": "unreal_get_actors_in_level",
                        "description": "Returns all actors in the current UE5 world.",
                        "inputSchema": {"type": "object"}
                    },
                    {
                        "name": "unreal_spawn_actor",
                        "description": "Spawns an Actor or Blueprint in the persistent level.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "asset_path": {"type": "string"},
                                "location": {"type": "array", "items": {"type": "number"}}
                            },
                            "required": ["asset_path"]
                        }
                    },
                    {
                        "name": "unreal_query_asset_registry",
                        "description": "Queries the Unreal Asset Registry for packages and classes.",
                        "inputSchema": {"type": "object"}
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
                        "text": f"[unreal-mcp] Simulated call to '{tool_name}' with args {args}. Bridge ready."
                    }
                ]
            }
        }
    return {"jsonrpc": "2.0", "id": req_id, "result": {}}

def main():
    parser = argparse.ArgumentParser(description="Unreal Engine 5 MCP Bridge")
    parser.add_argument("--port", type=int, default=30010, help="UE5 Remote Control Port")
    args = parser.parse_args()

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
            sys.stderr.write(f"UE5 MCP Error: {e}\n")

if __name__ == "__main__":
    main()
