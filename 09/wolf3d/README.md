# Wolfenstein 3D — id Software, 1992

**Source:** https://github.com/id-Software/wolf3d (GPL)

The first step. Raycasting through a grid of square rooms — no BSP, no arbitrary geometry, no height variation. Every wall is the same height. Every corridor meets at 90 degrees. The illusion of 3D produced entirely by math on a flat grid.

Read this first. See how much is hardcoded, how much is constraint mistaken for design. Then open Doom and feel the ground shift.

## What to read

- `WL_DRAW.C` — the raycaster. This is the entire visual engine.
- `WL_GAME.C` — the game loop
- `WL_MAP.C` — how levels are stored (flat arrays, not BSP)

## The constraint it breaks in Doom

Rooms cannot be stacked. Walls cannot slope. The player cannot look up or down. These are not engine limitations — they are assumptions baked so deep they look like physics.
