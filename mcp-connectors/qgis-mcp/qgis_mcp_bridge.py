#!/usr/bin/env python3
"""
qgis_mcp_bridge.py - Model Context Protocol Bridge for QGIS Desktop
Connects AI agents to the QGIS MCP plugin on port 9877.
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
                        "name": "qgis_export_heightmap",
                        "description": "Exports a QGIS DEM raster as a 16-bit grayscale PNG heightmap for game engines.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "layer_name": {"type": "string"},
                                "output_path": {"type": "string"},
                                "target_resolution": {"type": "array", "items": {"type": "integer"}}
                            },
                            "required": ["output_path"]
                        }
                    },
                    {
                        "name": "qgis_calculate_slope_mask",
                        "description": "Generates slope and aspect splatmasks for procedural terrain texturing.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "min_angle": {"type": "number"},
                                "output_path": {"type": "string"}
                            },
                            "required": ["output_path"]
                        }
                    },
                    {
                        "name": "qgis_export_vector_splines",
                        "description": "Exports roads, trails, or rivers as GeoJSON splines for engine path generation.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "feature_type": {"type": "string", "enum": ["roads", "rivers", "contours"]},
                                "output_path": {"type": "string"}
                            },
                            "required": ["output_path"]
                        }
                    },
                    {
                        "name": "qgis_run_pyqgis",
                        "description": "Executes raw PyQGIS code in the active QGIS Desktop canvas.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {"code": {"type": "string"}},
                            "required": ["code"]
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
                        "text": f"[qgis-mcp] Simulated execution of '{tool_name}' with args {args}. Bridge ready on port 9877."
                    }
                ]
            }
        }
    return {"jsonrpc": "2.0", "id": req_id, "result": {}}

def main():
    parser = argparse.ArgumentParser(description="QGIS MCP Bridge Server")
    parser.add_argument("--port", type=int, default=9877, help="QGIS TCP Socket Port")
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
            sys.stderr.write(f"QGIS MCP Error: {e}\n")

if __name__ == "__main__":
    main()
