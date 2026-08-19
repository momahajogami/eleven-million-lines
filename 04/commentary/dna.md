# Blender's DNA — The Data Model

Blender stores every scene, every object, every material, every animation curve in a unified binary format called `.blend`. The specification for that format lives entirely in `source/blender/makesdna/`. The files there are C header files — structs, enums, and a few macros — and they define, exhaustively, every data type that Blender can save.

This system is called **DNA**. The runtime layer that generates accessor code from those definitions is called **RNA**. You do not need to understand RNA to read DNA, but knowing the pair exists helps: DNA is the schema, RNA is the introspection layer built on top of it.

---

## Where to start

Open `source/blender/makesdna/DNA_object_types.h`. It is 790 lines. It defines `Object` — the struct that represents anything in a Blender scene: a mesh, a camera, a light, an empty, a curve, an armature. Every object you have ever seen in a Blender viewport is one of these.

The first thing to notice: `Object` has an `ID` at the top. Every datablock in Blender — every mesh, material, texture, armature, action — starts with an `ID`. The `ID` struct is defined in `DNA_ID.h` and it contains the name, the user count (how many other datablocks reference this one), and flags. Everything in Blender that can be named, linked, and referenced is an `ID`.

This is the unifying principle of the data model. Meshes, materials, cameras, curves — they are all `ID` subtypes. When you link an asset from one `.blend` file into another, you are copying an `ID`. When you create a duplicate, you are incrementing a user count.

---

## The mesh

Open `DNA_mesh_types.h` (597 lines). The `Mesh` struct is what you are working with when you model. For most of Blender's history, it stored four arrays:

- `MVert` — vertices (position, normal, weight)
- `MEdge` — edges (two vertex indices, flags)
- `MLoop` — loops (a vertex index plus an edge index; one loop per corner of a polygon)
- `MPoly` — polygons (an offset into the loop array plus a count)

This is not the most intuitive representation if you have only worked with simple triangle meshes, but it is flexible: polygons can have any number of sides, and the loop structure handles UV coordinates, vertex colors, and other per-corner data cleanly.

Recent versions of Blender migrated to a custom attribute system backed by arrays of arbitrary type — the `CustomData` fields you will see in the struct. The old MVert/MEdge/MLoop/MPoly structs are still present for compatibility. You are reading a struct that has been extended carefully, across decades, without breaking the format.

---

## The dependency graph

Blender's dependency graph (`source/blender/depsgraph/`) is the system that decides, when you change one thing, what else needs to update.

Move a bone: what changes? The mesh it deforms. The shape of the mesh in the viewport. The bounding box. The data the render engine reads. The dependency graph tracks all of these relationships and propagates updates efficiently.

The public API is in `DEG_depsgraph.hh`. The implementation is in `depsgraph/intern/`. This is the system that makes Blender feel responsive with complex scenes: instead of recalculating everything when anything changes, the graph recalculates only what the change affects.

For a creative tool used by artists, this is not a performance optimization. It is the difference between a tool you can think with and one you cannot.

---

## The `.blend` file format

The `.blend` format is documented at https://wiki.blender.org/wiki/Development/Architecture/BlendFile, but you can derive most of it from the source. The format writes the DNA structs directly to disk — not serialized to JSON or XML, but as raw binary representations of the C structs, with a catalog of the struct definitions appended at the end so the loader can reconstruct them even if the struct layout has changed.

This means a `.blend` file is self-describing. If you write a Blender file today and open it in a version of Blender from five years ago, the loader can read it — it has the struct definitions from both versions and can map fields between them. This is why your old project files still open.

It is also why the DNA headers are the spec. The file format documentation is the headers.

---

## What to do

1. Open `DNA_object_types.h`. Find the `Object` struct. Count how many fields it has. Find the field that determines which scene collection it belongs to. Find the field that holds its material override.

2. Open `DNA_mesh_types.h`. Find `Mesh`. Trace how vertex positions are stored — through `CustomData` to the float array underneath.

3. Open a small `.blend` file in a hex editor. Find the `BLENDER` file header. After the file blocks, find the `DNA1` block — it contains the struct catalog. Compare what you see there to the headers.

4. The 2.8 redesign of Blender (2018–2019) restructured the viewport, the object model, and the dependency graph simultaneously. Read the `CHANGELOG` entries for 2.80 with `DNA_object_types.h` open. The struct changes tell you what the redesign actually did.
