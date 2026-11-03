#!/usr/bin/env python3
"""
blender_prop_generator.py
Autonomous Blender 3D Prop Generator for Master Game Studio Skills
Can run headlessly via: blender --background --python blender_prop_generator.py -- [output_path]
"""

import sys
import math

try:
    import bpy
    import bmesh
except ImportError:
    print("[!] This script is meant to be executed inside Blender's Python environment.")
    print("    Example: blender --background --python blender_prop_generator.py")
    sys.exit(0)

def clear_scene():
    """Wipes all existing meshes, lights, and cameras."""
    bpy.ops.wm.read_factory_settings(use_empty=True)

def create_modular_chest(output_path="chest.gltf"):
    """Procedurally creates a stylized modular dungeon chest."""
    clear_scene()
    
    # 1. Base Box
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.4))
    base = bpy.context.active_object
    base.name = "Chest_Base"
    base.scale = (1.4, 0.9, 0.7)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    
    # 2. Lid (Half Cylinder)
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=16,
        radius=0.45,
        depth=1.4,
        rotation=(0, math.radians(90), 0),
        location=(0, 0, 0.75)
    )
    lid = bpy.context.active_object
    lid.name = "Chest_Lid"
    
    # Join into single prop
    bpy.ops.object.select_all(action='DESELECT')
    base.select_set(True)
    lid.select_set(True)
    bpy.context.view_layer.objects.active = base
    bpy.ops.object.join()
    
    # 3. Add Bevel Modifier
    bev = base.modifiers.new(name="Bevel", type='BEVEL')
    bev.width = 0.03
    bev.segments = 2
    bpy.ops.object.modifier_apply(modifier="Bevel")
    
    # 4. Smart UV Unwrap
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.uv.smart_project(angle_limit=66.0, island_margin=0.03)
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # 5. PBR Material Setup
    mat = bpy.data.materials.new(name="M_Chest_Stylized")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf:
        # Warm wood tone with slight roughness
        bsdf.inputs['Base Color'].default_value = (0.25, 0.14, 0.08, 1.0)
        bsdf.inputs['Roughness'].default_value = 0.65
    base.data.materials.append(mat)
    
    # 6. Export to glTF 2.0
    print(f"[*] Exporting glTF to: {output_path}")
    bpy.ops.export_scene.gltf(
        filepath=output_path,
        export_format='GLTF_SEPARATE',
        export_apply=True
    )
    print("[+] Chest prop generated successfully!")

if __name__ == "__main__":
    out = "modular_chest.gltf"
    if "--" in sys.argv:
        args = sys.argv[sys.argv.index("--") + 1:]
        if args:
            out = args[0]
    create_modular_chest(out)
