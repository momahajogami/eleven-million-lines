# DOOM — id Software, 1993

**Source:** https://github.com/id-Software/DOOM (GPL)

The middle step. Arbitrary wall angles, variable floor and ceiling heights, the WAD file format, and BSP trees as the solution to a rendering problem that would otherwise be unsolvable in real time on 1993 hardware.

Still not true 3D — rooms cannot stack, players cannot look up or down — but the assumptions have cracked. The geometry is no longer a grid. The world is now a graph.

## What to read

- `r_bsp.c` — the BSP traversal. This is the heart of the renderer.
- `p_map.c` — collision detection and movement
- `w_wad.c` — the WAD loader. Data-driven design before the term existed.
- `p_inter.c` — interaction and damage. How the game model works.

## The WAD format

Levels, textures, sounds, and sprites are all in the WAD file. The engine is separate from the data. This is why Doom is still being modded thirty years later — the data format outlasted the hardware it ran on.

## The constraint it breaks in Quake

The world is still flat. Height is simulated, not real. One more assumption left to shed.
