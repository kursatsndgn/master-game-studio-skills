# Procedural Dungeon & Map Generation (`procedural-dungeon.md`)
# Integrations: watabou (procedural generators), modly (modular tile placement)
# Sub-Agent Domain: @engine-developer

## 1. Overview & `watabou` Pipeline
`watabou` produces algorithmic JSON and SVG graphs representing dungeons, city layouts, and regional maps. This pipeline ingests watabou data structures and maps them deterministically into 3D level geometry in Godot 4 (GridMap) or Unity (Tilemap/Prefab Spawner).

```text
watabou JSON Map Data --> Cell Parser & Connectivity Graph --> Modly Modular Tile Mapping --> Godot GridMap / Unity Instancer
```

---

## 2. Watabou JSON Ingestion Schema

```json
{
  "dungeon": {
    "rooms": [
      {"id": 0, "x": 4, "y": 4, "w": 8, "h": 6, "type": "ENTRANCE"},
      {"id": 1, "x": 16, "y": 4, "w": 10, "h": 8, "type": "BOSS_CHAMBER"}
    ],
    "corridors": [
      {"from": 0, "to": 1, "waypoints": [{"x": 12, "y": 6}, {"x": 16, "y": 6}]}
    ]
  }
}
```

---

## 3. Godot 4 GridMap Generation Script (GDScript)

```gdscript
extends Node3D
class_name DungeonBuilder

@export var grid_map: GridMap
@export var wall_mesh_id: int = 0
@export var floor_mesh_id: int = 1
@export var door_mesh_id: int = 2

func generate_from_watabou_data(data: Dictionary) -> void:
    grid_map.clear()
    
    # Place Room Floors and Walls
    for room in data.get("dungeon", {}).get("rooms", []):
        var rx: int = room["x"]
        var ry: int = room["y"]
        var rw: int = room["w"]
        var rh: int = room["h"]
        
        for x in range(rx, rx + rw):
            for z in range(ry, ry + rh):
                # Floor Tile
                grid_map.set_cell_item(Vector3i(x, 0, z), floor_mesh_id)
                
                # Perimeter Walls
                if x == rx or x == rx + rw - 1 or z == ry or z == ry + rh - 1:
                    grid_map.set_cell_item(Vector3i(x, 1, z), wall_mesh_id)

    print("[DungeonBuilder] Generated procedural layout successfully!")
```
