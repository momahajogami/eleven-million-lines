# Commentary

This directory is the annotation layer for Unit 03. The repo it sits beside is a primary text — it is not modified. Everything here lives alongside it.

---

## Structure

```
commentary/
└── blender/
    ├── entry.md        ← start here: the architecture, the door in
    ├── bpy.md          ← the Python API layer: how Blender exposes itself
    ├── render.md       ← the render pipeline: Cycles, EEVEE, what's underneath
    ├── depsgraph.md    ← the dependency graph: how Blender thinks about change
    ├── dna_rna.md      ← DNA/RNA: Blender's data model, one of its strangest ideas
    └── ...
```

---

## Format

Each commentary file follows the same loose structure:

1. **The numbers** — size, scope, what you're about to hold
2. **The code** — quoted directly, the relevant passage
3. **The reading** — what it does, why it matters, what to notice
4. **The connections** — what this links to, in the repo or outside it
5. **The moment** — one sentence: what the student should feel here

The code is always quoted rather than linked. The reader should not have to leave the page to see what is being discussed. This is how Lions did it. It works.

---

## Voice

These files have a point of view. They are not neutral summaries. They say "this is beautiful" when something is beautiful and "this is strange" when something is strange. They are written to be read, not consulted.

Short. Precise. Opinionated. Signed by the course.

---

## What these become

Every commentary file is a course asset. It can become:

- The basis for a lecture
- A discussion prompt
- A handout for Track A or Track B students
- An easter egg dropped into the repo for students to find

The exploration and the course-building are the same act. Reading carefully and writing about what you find is how the course gets made.

---

## A note on Blender specifically

Blender is not old code. It is not spare code. It is a million-line C/C++ codebase written by hundreds of contributors over thirty years, and it shows. The commentary here does not pretend otherwise. The task is not to make it feel small — it is to find the load-bearing ideas and stand next to them long enough to understand why they are there.

The DNA/RNA system alone is worth a week. So is the dependency graph. So is the history of the render pipeline from Blender Internal to Cycles. This unit asks: what does it look like when open-source creative software grows up?
