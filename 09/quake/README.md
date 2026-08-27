# Quake — id Software, 1996

**Source:** https://github.com/id-Software/Quake (GPL)

The realization. True 3D geometry. Rooms that stack. Players who can look anywhere. A physics engine. A scripting language (QuakeC) so players can mod without touching the engine. And under all of it, the algorithms: BSP trees grown more sophisticated, the fast inverse square root (`Q_rsqrt`), a renderer doing by hand what GPUs now do automatically.

## The algorithm arc ends here

- **Wolf3D**: raycasting — O(width) per frame, no spatial index
- **Doom**: BSP traversal — subdivide space, render front-to-back, never draw what's hidden
- **Quake**: BSP + PVS (Potentially Visible Set) — precompute what can see what, discard the rest before the frame begins

Each step is a new answer to the same question: how do you decide what not to draw?

## What to read

- `gl_rsurf.c` / `r_bsp.c` — the BSP renderer
- `common.c`: `Q_rsqrt` — the fast inverse square root. Read the comment. Read the constant. Read Carmack's note.
- `sv_phys.c` — the physics engine
- `progs.c` — the QuakeC virtual machine
- `world.c` — the entity and collision system

## Companion reading

- Michael Abrash, *Graphics Programming Black Book* — free online; Abrash was at id during Quake
- Carmack's .plan files, 1995–2000 — the thinking-in-public that produced this code
