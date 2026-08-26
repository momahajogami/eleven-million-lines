# Quake and the Shape of Space

*A bridge from Unit 07 toward what comes next*

---

## The Problem Carmack Was Solving

It is 1993. id Software is in Mesquite, Texas. John Carmack is trying to render a three-dimensional world in real time on a 33 MHz computer with no hardware graphics acceleration.

This is not a mathematics problem. It is a physics problem, a geometry problem, a topology problem — wearing an engineering costume, with a Christmas deadline.

The question Carmack is asking is the same question that fills Unit 07, in different language: *what is the shape of this space, and how do I move through it?*

---

## What Space Quake Lives In

A Quake map is a three-dimensional region carved out of solid stone by a process called Constructive Solid Geometry (CSG). You begin with a universe filled with solid matter. You subtract half-spaces — regions defined by planes. What remains after the subtraction is the room.

This is the same operation that appears in algebraic geometry when you define a variety as the solution set of equations. You subtract. What survives is the shape.

The Quake map file describes this in terms of *brushes*: convex regions bounded by planes, the same half-spaces you meet in linear programming and convex geometry. The level geometry is a Boolean combination of these half-spaces. Intersection, union, complement. The same operations that define simplicial complexes — just wearing a different hat.

---

## BSP Trees: Recursively Partitioning the World

Carmack needed to know, for every frame, which walls were in front of which other walls — the painter's algorithm, deciding what to draw in what order so the near things occlude the far things.

His solution: the **Binary Space Partition tree**.

Choose a plane. Divide the world into front and back. Recurse on each side. The result is a binary tree where every node is a plane and every leaf is a convex region of space.

This is a topological decomposition. The BSP tree imposes a structure on space — a cell decomposition, a partition into regions with well-defined adjacency. If you squint, it is a CW complex: cells (the convex leaves), faces between them (the cutting planes), an adjacency structure that tells you which cells share a boundary.

Grothendieck's insight was that topology can be extracted from algebraic structure — from the equations, without looking at the geometry. Carmack's insight was the engineering dual: if you impose enough structure on the geometry, the topology becomes navigable in real time.

---

## The Fast Inverse Square Root

In `q_math.c`, there is a function:

```c
float Q_rsqrt(float number)
{
    long i;
    float x2, y;
    const float threehalfs = 1.5F;

    x2 = number * 0.5F;
    y  = number;
    i  = * ( long * ) &y;
    i  = 0x5f3759df - ( i >> 1 );
    y  = * ( float * ) &i;
    y  = y * ( threehalfs - ( x2 * y * y ) );

    return y;
}
```

The magic constant `0x5f3759df`. The bit manipulation treating a float as an integer. One iteration of Newton's method. A result accurate to within 1% in a fraction of the time a real square root takes.

This works because of the geometry of floating-point representation. The exponent bits of an IEEE 754 float encode a logarithm. Shifting right by one is approximately dividing the logarithm by two — which is approximately taking the square root. The constant corrects for the offset.

It is a hack that works because someone understood the structure of the thing they were hacking. The mathematics underneath is real. The manipulation is precise. This is what Grothendieck would call — if he had been the sort of person who played Quake — an étale morphism: a local isomorphism between structures that looks strange globally but is completely well-behaved locally.

---

## Carmack's .plan Files

While Grothendieck was writing *Récoltes et Semailles* — a thousand-page document of mathematical autobiography and spiritual reckoning — John Carmack was writing `.plan` files.

A `.plan` file is a Unix convention: a text file in your home directory, readable by anyone who ran `finger username@hostname`. Carmack used his as a dev diary. Posted when he thought of something. Thousands of people read them.

They are mathematical thinking in public. Not formal. Not polished. Not waiting to be complete before being shared. The same spirit as a Grothendieck notebook, but faster, louder, and shipping by Christmas.

Both men worked in public. Both made things that lasted. The difference in style — the monk and the Texan — is a difference in what mathematics is *for*.

---

## The Topology Underneath

Euler characteristic: in a Quake map, count the convex cells (V), the planes between them (E, loosely), and the enclosed regions (F). The alternating sum is a topological invariant of the level. Two levels with different Euler characteristics are not homeomorphic — they are genuinely different shapes.

The homology of a Quake level tells you how many rooms it has (H₀), how many loops you can walk without backtracking (H₁), how many fully enclosed chambers exist (H₂).

The mapper who built the level probably did not think in these terms. But the structure is there regardless. The mathematics is not imposed — it is found.

---

## Why Quake Belongs Here, and Also Somewhere Else

Unit 07 is about abstraction: the shape of things as seen from far away, through algebra, through category theory, through the patient work of building tools that see structure where others see fog.

Quake is the same questions asked at speed, under constraint, by someone who needed to ship.

Both are legitimate ways to understand space. Together they make a conversation.

A full Quake unit — the source drop as an act, the .plan files as a dev diary, the fast inverse square root, the BSP tree as a curriculum in applied topology, Carmack versus Romero as a character study in what it costs to finish something — belongs somewhere in this course. Probably after Unit 07. Possibly as Unit 09, after Unit 08 builds simplices by hand and asks: now what do we build with them?

Carmack knew. He built a world.

---

## Characters

**John Carmack** — the engine. Thinks in first principles. Rebuilt the graphics pipeline every game because the previous solution was no longer interesting. His .plan files from 1995–2000 are among the best technical writing of the decade, unedited, unasked-for, free.

**John Romero** — the game. Carmack built what the machine could do; Romero built what it felt like to be inside it. Their split after Quake is one of the great creative-partnership stories in software history.

**Michael Abrash** — the mathematician in the room. Wrote *Zen of Assembly Language* and *Graphics Programming Black Book*, which are the best explanations of what Quake's engine is doing and why. Still the clearest guide to applied graphics mathematics ever written.

**The demoscene** — the community that was doing real-time 3D before id, faster, on worse hardware, as art. The context Quake emerged from. Mostly invisible in the popular history. The demo scene's relationship to Quake is the same as the underground's relationship to any major act: they were there first, they were better in some ways, they never got the credit.

---

*The source code for Quake was released under the GPL in 1999. It is small enough to read. It is old enough to be historical. It is written by someone who understood, deeply, the shape of the space he was building.*

*That is enough to make it ours.*
