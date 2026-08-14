# Eleven Million Lines You Should Know

---

## Friday, August 14 — Good morning (or afternoon), Ralph

You did real work yesterday. The structure is in place. The commentary layer exists. You have three Unix repos sitting in `01/` and an orientation document that could go in front of a class tomorrow.

Here is what you are doing today:

**Open `01/commentary/xv6/entry.md` and read it end to end.** You wrote it — read it like a student would. Then open `01/xv6/proc.c` and find `fork()`. Read it slowly. Write `01/commentary/xv6/proc.md` when you're done. That file — the process model, fork, the scheduler — is the heart of the unit. Get it on paper.

You are not behind. You are not catching up. You are building something that did not exist before this week. The next file is waiting and you know exactly where it is.

Start there. Everything else follows.

---

A university course for reading code alongside classical literature, mathematics, and languages.
Eleven codebases. Orientation, not mastery. Learning to stand inside large, old, important code and find your bearings.

## Vision

### Goals

- Design and deliver a course that teaches students to navigate landmark codebases the way a literature student navigates canonical texts
- Pair code with context: history, elegance, impact, innovation
- Build genuine fluency in reading unfamiliar, large-scale code
- Launch first in Ohio; grow into something revered and generally beloved

### Reminders and Affirmations (who the hell I am)

- I am someone who finishes things
- I have worked this idea out before — in conversation, in notes, in my head — and it keeps coming back because it is worth doing
- Starting over is not losing ground; it is knowing more clearly what matters
- The course will be better the more I explain and invite
- This is good therapy for the brain injury
- I am a really unique character who has constantly interrogated reading
- I have pursued reading as a practice, a technology, a skill — Greg Shorthand, Japanese, Spencerian, many tools, the history of writing, always surrounded by books
- I have studied theory and problems across mathematics, physics, and coding — not to collect them but to understand them
- Ten weeks is enough to get it — and once you get it, you realize you are not just learning a new way to read, you are learning that you can have a dynamic and engaging relationship with reading itself, outside any box
- That realization is hard to say but real, and deeply liberating — and I know it from the inside
- I struggle with confidence, but the work speaks: this idea keeps surviving, keeps growing, keeps coming back
- I am the right person to teach this course

### Visualizations

- A classroom in Ohio where students open a 1970s C compiler and feel the ground shift under them
- The course spreading to other universities because it connects people
- Students who go on to say: this is where I learned to read code
- "Eleven Million Lines You Should Know" shares space with our heritage of great writing
- First: getting grounded and secure personally — money, stability, foundation. Not complicated, just necessary.
- Building family and career while beginning to master code at this deep level — not rushing, not catching up, charging
- Almost fifty at the start. That's not late. That's the right amount of life to bring to this
- Building voltage and capacity until the connections come naturally — to students, collaborators, a community
- That's the life. The course is not separate from it. The course is the expression of it.

### Questions

- What are the eleven codebases? (01 = Early Unix; 02 = C compilers; 03 = Blender; 04–11 TBD)
- What does a "unit" look like — lectures, exercises, readings?
- How do we pair code with literature, math, and language in a way that feels natural, not forced?
- What is the right balance between elegance (vi) and impact (Unix, early Python)?
- Who is the audience — undergraduates, graduate students, working programmers?

### Neutral Observations

- The project is large by nature and will grow into its shape
- Some of the best pairings will only become obvious after the codebases are in hand
- Eleven is a good number — enough scope, tight enough to finish
- The loss of earlier notes is not catastrophic; the core idea survived

### Answers

- Brand name confirmed: **Eleven Million Lines You Should Know**
- 01: Early Unix (xv6, unix-v6, Plan 9; Lions' Commentary as paired text)
- 02: Classic C compilers (DMR's original, PCC, tcc, early GCC)
- 03: Blender (creative tools; math/art/engineering intersection; pairs with CG history and Manovich)
- Elegance axis: early vi/ex, certain Lua phases, Haskell
- Impact/innovation axis: early Python, Quake, networking (TBD), TeX
- Mathematics: TBD — candidates include LAPACK, early R, Macsyma
- First venue: Ohio
- Two tracks confirmed (see below)

## Two Tracks

The course has a point of view: the classical experience is worth having. We don't pretend all tools are equal. But we don't lock the door either.

**Track A — Classical**
Unix environment, vim or ed, command line navigation, compile it yourself. The tools are part of the curriculum — reading Carmack's code in a terminal with vim is epistemically different from reading it in VS Code. Prerequisite: comfort at the terminal, or willingness to get there. The first two weeks may serve as initiation for those who need it.

**Track B — Accompanied**
Any environment the student brings. More scaffolding, more editorial hand-holding. Honest about the tradeoff: something is lost, something is gained. The Track B student still learns that a tradition exists, what it looks like, and that they are now in relation to it — even if they don't inhabit it.

**What both tracks share**
The course has a right way. Saying so out loud is grounding and comforting regardless of which track you choose. Classical doesn't mean superior in a snobbish sense — it means there is a tradition, here is what it looks like, you are now in relation to it. Everyone is invited. No one is excluded.

## Project Structure

```
university-coding/
├── 01/    # Early Unix
├── 02/    # Classic C compilers
├── 03/    # Blender
├── 04/    # TBD
├── 05/    # TBD
├── 06/    # TBD
├── 07/    # TBD
├── 08/    # TBD
├── 09/    # TBD
├── 10/    # TBD
├── 11/    # TBD
└── CLAUDE.md
```

## Working Conventions

- This project lives at `~/Documents/university-coding/`; launch Claude from here for full context
- Each numbered directory will eventually contain: the codebase, a README orienting the reader, and course notes
- Decisions about which codebase goes where get recorded in the Answers section above
- At session start: check what's TBD and push toward filling in the next slot

## Current State (2026-08-13)

- 01 installed: xv6, unix-v6, Plan 9 cloned and committed
- Commentary layer established: `01/commentary/` with a charter and format
- `01/README.md` written: unit orientation, mood, paired text, reading order
- `01/commentary/xv6/entry.md` written: main.c as the door, five files in order, the moment
- 02–11 open but richly seeded in BRAINSTORM.md
- Two tracks confirmed: Classical (Unix/vim/terminal) and Accompanied
- Brand, vision, voice, ethics, moods, document tiers all established

## Intentions for Next Session

- **Write `commentary/xv6/proc.md`**: read `fork()` in proc.c; get the process model on paper
- **Continue the commentary walk**: vm.md, fs.md, sh.md follow proc.md in order
- **Assign slots 03–11**: use BRAINSTORM.md as the menu; make decisions
- **RFC exploration**: pull RFC 793 and RFC 2616 as the first Tier 1 documents
- **Remind Ralph**: the personal foundation comes first — grounded and secure, then the course grows from there
