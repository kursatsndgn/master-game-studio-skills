#!/usr/bin/env python3
"""
unity_mcp_bridge.py - Model Context Protocol Bridge for Unity Editor
Communicates with Unity Editor on port 8080.
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
                        "name": "unity_get_scene_hierarchy",
                        "description": "Inspects active Unity Scene GameObjects and attached components.",
                        "inputSchema": {"type": "object"}
                    },
                    {
                        "name": "unity_instantiate_prefab",
                        "description": "Instantiates a Prefab asset into the active scene.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "prefab_path": {"type": "string"},
                                "position": {"type": "array", "items": {"type": "number"}}
                            },
                            "required": ["prefab_path"]
                        }
                    },
                    {
                        "name": "unity_refresh_asset_database",
                        "description": "Forces Unity to re-import newly created external files.",
                        "inputSchema": {"type": "object"}
                    },
                    {
                        "name": "unity_run_playmode_test",
                        "description": "Executes automated Playmode test suites in Unity.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {"test_suite": {"type": "string"}}
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
                        "text": f"[unity-mcp] Simulated call to '{tool_name}' with args {args}. Bridge ready."
                    }
                ]
            }
        }
    return {"jsonrpc": "2.0", "id": req_id, "result": {}}

def main():
    parser = argparse.ArgumentParser(description="Unity MCP Bridge")
    parser.add_argument("--port", type=int, default=8080, help="Unity MCP port")
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
            sys.stderr.write(f"Unity MCP Error: {e}\n")

if __name__ == "__main__":
    main()
