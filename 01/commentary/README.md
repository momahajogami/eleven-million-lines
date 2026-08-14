# Commentary

This directory is the annotation layer for Unit 01. The repos it sits beside are primary texts — they are not modified. Everything here lives alongside them, the way Lions' Commentary lived alongside the V6 source.

---

## Structure

Each subdirectory corresponds to a repo:

```
commentary/
├── xv6/
│   ├── entry.md        ← start here
│   ├── proc.md         ← the process model: fork, exit, wait, scheduler
│   ├── vm.md           ← virtual memory
│   ├── fs.md           ← the filesystem
│   ├── sh.md           ← the shell
│   └── ...
├── unix-v6/
│   └── ...
└── plan9/
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
