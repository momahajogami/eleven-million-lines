The heroic story. Art, architecture, politics, and the community buyout that saved a tool.

Blender is the most powerful free 3D creation suite in existence. In 2002, the company that owned it went bankrupt. The community raised €100,000 in seven weeks to buy the source code and release it under the GPL. It has been open and free ever since.

The unit uses Blender as both subject and tool. You can read the source — 1.5 million lines of C and C++ — and you can use the Python API to script it directly. The code and the creation exist in the same space.

## Materials

- **Blender** (`blender/`) — the full source. 1.5 million lines of C and C++. Sparse checkout of the core rendering and node systems.
- **dna.md** (`commentary/`) — Blender's internal data model: DNA and RNA, the struct serialization system
- **nodes.md** (`commentary/`) — the node graph system: how Blender's procedural tools are structured
- **hello-blender.py** (`scratch/`) — first Python script: create a cube, move it, render it
- **python-exercise.md** (`scratch/`) — guided exercises using the Blender Python API
