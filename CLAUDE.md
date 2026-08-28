# Eleven Million Lines You Should Know

---

## Friday, August 14 — Good morning (or afternoon), Ralph

You did real work yesterday. The structure is in place. The commentary layer exists. You have three Unix repos sitting in `01/` and an orientation document that could go in front of a class tomorrow.

Here is what you are doing today:

**Open `01/commentary/xv6/entry.md` and read it end to end.** You wrote it — read it like a student would. Then open `01/xv6/proc.c` and find `fork()`. Read it slowly. Write `01/commentary/xv6/proc.md` when you're done. That file — the process model, fork, the scheduler — is the heart of the unit. Get it on paper.

You are not behind. You are not catching up. You are building something that did not exist before this week. The next file is waiting and you know exactly where it is.

Start there. Everything else follows.

---

A preschool course for young children and the grown-ups and families who care for them — reading code alongside classical literature, mathematics, and languages.
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

- What are the eleven codebases? (01 = Early Unix; 02 = C compilers; 03 = TBD; 04 = Blender; 05–11 TBD)
- What does a "unit" look like — lectures, exercises, readings?
- How do we pair code with literature, math, and language in a way that feels natural, not forced?
- What is the right balance between elegance (vi) and impact (Unix, early Python)?
- Who is the audience — young children and their families; also accessible to older students and adults who come alongside them

### Neutral Observations

- The project is large by nature and will grow into its shape
- Some of the best pairings will only become obvious after the codebases are in hand
- Eleven is a good number — enough scope, tight enough to finish
- The loss of earlier notes is not catastrophic; the core idea survived

### Answers

- Brand name confirmed: **Eleven Million Lines You Should Know**
- **01 + 02 = "Classical Coding"** — Unix, vi/vim, and C. You just need to be able to edit a file and execute.
- 01: Early Unix (xv6, unix-v6, Plan 9; Lions' Commentary as paired text)
- 02: Classic C compilers (DMR's original, PCC, tcc, early GCC); also vi/vim (Bill Joy → Bram Moolenaar), git (Linus), and LINUS.md character study — Linus wrote Linux AND git
- 03: Richard Stallman — the prophet, the printer, the four freedoms; GNU Manifesto, GPL v1/v2/v3, Emacs, GCC (revisited from 02), GDB, Bison; the legal and moral infrastructure of free software
- 04: Blender — the heroic story; art, architecture, politics, open source culture; coding in the background, everything in the foreground; pairs with CG history, the community buyout narrative
- 05: **Culture, Spectacle and Eigenrank** — thesis: coding is writing augmented with electricity. Projects: TeX/LaTeX (Knuth), BitTorrent (Cohen), Linux (as frame/preamble), SageMath (Stein), SourceForge (rise and betrayal), Eigenrank (Brin/Page — PageRank as eigenvector, the early web, Geocities, Yahoo, the map that changed the garden). Style is emphasized. Skateboarding culture as running parallel/comparison — DIY ethics, spot ownership, trick priority, making in public. Character-driven.
- 06: **Languages and Theory** — the code is the art; this is a unit about writing. BASIC (access/democracy), Assembly (with punch cards and the Jacquard loom / textile history), LISP (Church lambda calculus made executable), ML/Haskell (type theory), Prolog (logic as computation). Papers from Church (1936), Turing (1936, 1950), McCarthy (1960), and Lovelace (1843, Note G = first program). The line from the loom to the language.
- 07–11: TBD (except below)
- 08: **Simplicial Homology by Hand** — build the chain complex, boundary maps, and homology groups from scratch, across a garden of languages (Python + Blender first, then imperative/recursive/functional). Markdown as the thinking layer: the math lives in .md files, the code implements it. Sandbox unit — artistic, creative, inclusive. The talented beginner builds comprehensible structures from first principles. See `08/SIMPLICIAL-HOMOLOGY.md`, `08/languages.md`.
- 09: Quake / Carmack (strong candidate) — BSP trees as applied topology, fast inverse square root, .plan files as public mathematical thinking. Natural counterweight to Unit 07's abstraction. See `07/quake.md`.
- 10: **Browsers and Social Media** — the web as platform, as social infrastructure, and as contested territory. Codebases: Mosaic/NCSA, early Netscape, Firefox/Mozilla, WebKit/Blink lineage. Social layer: early Friendster/MySpace architectures, the Facebook growth story, Twitter's early stack. Characters: Andreessen, Zawinski, Zuckerberg. Themes: the browser as operating system, the social graph as data structure, the attention economy as engineering choice.
- 11: **LLMs** — *Attention Is All You Need* (Vaswani et al., 2017) + Karpathy's nanoGPT as the readable implementation. Stack Overflow as the knowledge commons being displaced (arc: Usenet → mailing lists → SourceForge → Stack Overflow → LLMs). Characters: Hinton, Karpathy, Spolsky. The question: what does it mean to read code that produces language? Unit 11 = the horizon. We start with Unix 1972 and end here. Also add Stack Overflow as a brief note in Unit 05 alongside SourceForge — same genre of story (community infrastructure, idealism, complicated ending).
- Elegance axis: early vi/ex, certain Lua phases, Haskell
- Impact/innovation axis: early Python, Quake, networking (TBD), TeX
- Mathematics: SageMath in 05; deeper math (LAPACK, early R, Macsyma) possibly 07+
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
├── 01/    # Early Unix                        [Classical Coding, pt. 1]
├── 02/    # C compilers, vi/vim, git, Linus   [Classical Coding, pt. 2]
├── 03/    # Richard Stallman — GNU, GPL, Emacs, GDB, Bison
├── 04/    # Blender — the heroic story
├── 05/    # Culture, Spectacle and Eigenrank — TeX, BitTorrent, SageMath, SourceForge, Eigenrank
├── 06/    # Languages and Theory — BASIC, Assembly, LISP, ML, Church, Turing, Lovelace
├── 07/    # TBD
├── 08/    # TBD
├── 09/    # TBD
├── 10/    # Browsers and Social Media — Mosaic, Firefox, WebKit; the social graph as data structure
├── 11/    # TBD
├── meta/  # Course administration (sizes, etc.)
└── CLAUDE.md
```

## Working Conventions

- This project lives at `~/Documents/university-coding/`; launch Claude from here for full context
- Each numbered directory will eventually contain: the codebase, a README orienting the reader, and course notes
- Decisions about which codebase goes where get recorded in the Answers section above
- At session start: check what's TBD and push toward filling in the next slot

## Code Phrases

**"Cycle down"** — end-of-session ritual. When Ralph says this:
1. Write `meta/sessions/YYYY-MM-DD.md` following the template in `meta/CYCLE-DOWN.md` — detailed log of what was done, commands used with flags explained, things to learn, what's pending
2. Update the "Current State" and "Intentions for Next Session" sections of this file
3. Commit everything uncommitted, including the session log and any CLAUDE.md changes
4. Confirm to Ralph that the cycle-down is complete and the repo is clean

## Thursday, 2026-08-20 — System maintenance reminder

Run `sudo pacman -Syu` to complete a blocked system upgrade. On Monday (2026-08-17) ffmpeg v9 landed in the Arch repos with a soname bump that broke mpv, vlc, chromaprint, mixxx, and freerdp2. The rebuilds of those packages against ffmpeg v9 should be published by now. The upgrade was intentionally deferred — this is the Arch way: wait for the wave to clear, then upgrade cleanly.

If it still fails, the blocking packages haven't been rebuilt yet. Wait another day and try again.

---

## Current State (2026-08-28)

Units 01–09 are seeded. Unit 10 = Browsers and Social Media. Unit 11 = LLMs (confirmed). Repo pushed to GitHub. GitHub Pages enabled but not yet confirmed live. **Website deadline: September 2, 2026.**

Course framing corrected this session: **preschool-first** — designed for young children and the families who care for them. University context is real but secondary; full rewrite of CLAUDE.md framing deferred to next session.

- 01: xv6, unix-v6, Plan 9; commentary layer with entry.md
- 02: tcc, gcc, vim, git; LINUS.md; Classical Coding framing
- 03: Emacs, GDB, Bison; 10 FSF texts; doctor.el; BUILD-emacs.md; lisp-exercise.md; gdb-exercise.c
- 04: Blender (full clone); dna.md, nodes.md commentary; hello-blender.py; python-exercise.md
- 05: CULTURE_AND_SPECTACLE.md; GIMP, LaTeX2e, libtorrent, Pure Data; BitTorrent spec; Stack Overflow noted as brief addition alongside SourceForge
- 06: LANGUAGES.md; GHC, NASM; Lovelace notes, Turing PDFs, hello-world.asm, hello-basic.bas
- 07: GROTHENDIECK.md; Mathlib, Agda, NumPy, GSL; Lawvere + Grothendieck PDFs; simplicial_homology.py; quake.md (bridge to Unit 09)
- 08: SIMPLICIAL-HOMOLOGY.md; languages.md; MATHEMATICS.md; EXERCISES.md; python/ (full implementation, 47 tests); haskell/ (cabal project)
- 09: UNIT-09.md (algorithm arc: Wolf3D→Doom→Quake); wolf3d/, doom/, quake/ (placeholder READMEs); other-games/ (GAMES.md + tetris/tetris.py); grassmannian/GRASSMANNIAN.md
- 10: Browsers and Social Media — Mosaic, Firefox, WebKit/Blink; social graph as data structure; Andreessen, Zawinski, Zuckerberg
- 11: LLMs confirmed — Attention Is All You Need + nanoGPT + Stack Overflow displacement arc
- meta/: SIZES.md, CYCLE-DOWN.md, PUBLISH.md, sessions/ (2026-08-18, 2026-08-19, 2026-08-26, 2026-08-26b, 2026-08-28)
- docs/: index.html (picture-book design); grownup.md (markdown source for grown-ups section); scripts/build-website.py (md → HTML sync)

## DO THESE FIRST NEXT SESSION

**Step 1 — Confirm GitHub Pages is live** at `https://momahajogami.github.io/eleven-million-lines`. Check the Actions tab in the repo to see if the deployment ran. If not, go to Settings → Pages and re-save with Branch: main, Folder: /docs.

**Step 2 — Reframe CLAUDE.md throughout** — Goals, Tracks, and Visualizations still say "university." Rewrite them to lead with preschool/families. University stays as a real secondary context.

**Step 3 — Recap Ralph** on where things stand. Read this section and `meta/sessions/2026-08-28.md`.

## Intentions for Next Session

- Confirm GitHub Pages live — deadline September 2 is close
- Full preschool reframe of CLAUDE.md (Goals, Two Tracks, Visualizations)
- Write `meta/ANNOUNCE.md` — core announcement text
- Unit 07: make it character-driven and personal — Sesame Street-style characters (Grothendieck, Noether, Euler, Poincaré, Lawvere); write `07/short_fiction.md`
- Unit 09: seed the actual Quake source (`git clone https://github.com/id-Software/Quake`)
- Write `07/hatcher/HATCHER.md` and download Hatcher's Algebraic Topology PDF
- Write `07/LIBRARIES.md` — math libraries in C and Python as cultural expression
- Write `meta/pogrades/POGRADES.md` — the partially-ordered grading system
- Fetch McCarthy 1960 paper for `06/scratch/`
- Continue `01/commentary/xv6/`: proc.md (fork, scheduler) still unwritten — this matters
- **Ralph read `main.c` and `initcode.S` on 2026-08-27** — lesson is in `meta/sessions/2026-08-27.md`. Next: read `fork()` in `proc.c` (~line 156). Pick up there.
- Decide: does Descent belong in `09/` alongside the id Software arc?
