"""
hello-blender.py — your first Blender Python script

Run this inside Blender: open the Scripting workspace, paste this into
the text editor, and press Run Script. Or run from the command line:

    blender --background --python hello-blender.py

What this script does:
  1. Clears the default scene (cube, light, camera)
  2. Creates a grid of 5x5 UV spheres at different heights
  3. Assigns a material to each sphere with a procedural color
  4. Saves the result as /tmp/hello-blender.blend

This is not a useful script. It is a script that exercises the bpy API
enough that you can see how Blender is organized from Python's perspective.
"""

import bpy
import math


def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()


def make_material(name, r, g, b):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (r, g, b, 1.0)
    bsdf.inputs["Roughness"].default_value = 0.3
    return mat


def make_sphere(x, y, z, radius, material):
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=radius,
        location=(x, y, z),
        segments=32,
        ring_count=16,
    )
    obj = bpy.context.active_object
    obj.data.materials.append(material)
    return obj


def main():
    clear_scene()

    grid_size = 5
    spacing = 2.5

    for row in range(grid_size):
        for col in range(grid_size):
            # normalized position in [0, 1]
            t = (row * grid_size + col) / (grid_size * grid_size - 1)

            x = col * spacing - (grid_size - 1) * spacing / 2
            y = row * spacing - (grid_size - 1) * spacing / 2
            z = math.sin(t * math.pi * 2) * 1.5  # wave pattern

            r = t
            g = 1.0 - t
            b = math.sin(t * math.pi) ** 2

            mat = make_material(f"mat_{row}_{col}", r, g, b)
            make_sphere(x, y, z, 0.8, mat)

    # add a light
    bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
    bpy.context.active_object.data.energy = 3.0

    # add a camera
    bpy.ops.object.camera_add(location=(12, -12, 8))
    cam = bpy.context.active_object
    cam.rotation_euler = (math.radians(55), 0, math.radians(45))
    bpy.context.scene.camera = cam

    bpy.ops.wm.save_as_mainfile(filepath="/tmp/hello-blender.blend")
    print("Saved to /tmp/hello-blender.blend")
    print(f"Scene contains {len(bpy.data.objects)} objects")


main()
