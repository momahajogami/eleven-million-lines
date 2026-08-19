# Blender's Node Systems

Blender has three major node systems: the Shader Editor (material nodes), the Compositor, and Geometry Nodes. They share an architecture. Learning one is learning all three.

The shared architecture is not accidental. It is Blender's answer to a design problem: how do you give users a visual programming environment that is both expressive and consistent? The answer was to define a general node-graph system and implement each domain — shading, compositing, geometry — as a specialization of that system rather than a separate tool.

---

## Where the code lives

- `source/blender/nodes/` — the node type definitions for all three systems
- `source/blender/blenkernel/BKE_node.hh` — the shared node graph API
- `source/blender/makesdna/DNA_node_types.h` — the data structures (stored in `.blend`)
- `source/blender/editors/space_node/` — the node editor UI

Start with `DNA_node_types.h`. The key structs are `bNodeTree`, `bNode`, and `bNodeSocket`. A `bNodeTree` is a graph. `bNode` is a node in that graph. `bNodeSocket` is an input or output on a node. The connections between nodes are `bNodeLink` structs stored in the tree.

---

## The abstraction

Every node, in every domain, is registered as a `bNodeType`. The registration supplies callbacks: `execute` (what the node computes), `draw_buttons` (how it appears in the UI), `update` (called when connections change). The node graph system calls these callbacks; the specific shading or geometry logic lives in the callbacks, not in the graph engine.

Look in `source/blender/nodes/shader/nodes/` — each file is one shader node. `node_shader_mix.cc` is the Mix node you have probably used. It is short. The geometry equivalent is in `source/blender/nodes/geometry/nodes/`.

The brevity of individual node implementations is the design working: the graph machinery handles connectivity, dependency, and execution order. Each node only has to say what it computes.

---

## Geometry Nodes

Geometry Nodes (introduced in 2.92, 2021; substantially redesigned in 3.0 and 3.3) is the newest and most ambitious of the three systems. It gives the user access to Blender's geometry kernel — the same code that runs modifiers and simulations — through a visual programming interface.

A Geometry Nodes graph takes geometry as input and produces geometry as output. The nodes between can sample attributes, instantiate objects, run physics-style simulations, generate procedural patterns, and combine meshes in arbitrary ways. The result is a parametric modeling system: the graph describes how the geometry is constructed, not just what it looks like. Change an input parameter and the geometry regenerates.

The source for Geometry Nodes is in `source/blender/nodes/geometry/`. The geometry operations themselves — the actual algorithms — are in `source/blender/geometry/` (a separate library). The node implementations in the former call the algorithms in the latter. This is a clean separation: the node graph knows about data flow; the geometry library knows about mesh operations.

---

## Why this matters

Most creative software has scripting as an afterthought: a macro language bolted on after the tool was built, with limited access to the application's internals. Blender's node systems are the opposite — they are the primary interface for a significant portion of the tool's functionality, and they expose the underlying algorithms directly.

A Geometry Nodes graph is a program. It has inputs and outputs, data flow, conditionals (through switch nodes), and iteration (through simulation zones). A user building a procedural city generator in Geometry Nodes is writing a program that generates 3D geometry. The fact that it looks like a node graph rather than Python code does not change what it is.

This is consistent with Blender's general philosophy: the tool should be understandable from the inside. The shader graph, the compositor graph, and the geometry graph are all inspectable, modifiable, and sharable in the same way as any other data in a `.blend` file. They are not black boxes. They are documents.

---

## What to do

1. Open `DNA_node_types.h`. Read the definitions of `bNodeTree`, `bNode`, `bNodeSocket`, `bNodeLink`. Sketch the data structure on paper before reading further.

2. Open `source/blender/nodes/shader/nodes/node_shader_mix.cc`. This is the Mix shader node. Find where the mixing logic actually runs. Notice how little code there is.

3. Open `source/blender/nodes/geometry/nodes/node_geo_mesh_primitive_cube.cc`. This is the Cube node in Geometry Nodes — it generates a cube mesh. Find where the vertices are created. Compare the geometry generation code to `DNA_mesh_types.h` — you should see the same structs being populated.

4. In Blender, build a small Geometry Nodes graph: take a mesh input, scale it, output it. Then open the `.blend` file in a hex editor and find the `DNA1` block. The node graph you built is stored as `bNodeTree` / `bNode` / `bNodeSocket` / `bNodeLink` structs. The data you read in the code is the data in the file.
