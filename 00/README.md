# Eleven Million Lines You Should Know

*A university course about reading landmark codebases the way a literature student reads canonical texts — slowly, attentively, with historical and cultural context.*

---

## What this course is

You are going to read eleven codebases. Some of them are older than your parents. Some of them run on every computer on earth. Some of them changed what computers are, or what programming is, or who gets to do it.

You are not going to master them. No one masters them. Even the people who wrote them do not hold them fully in mind. The goal is orientation: to stand inside a large, old, important piece of code and find your bearings. To read it the way you would read a novel — with attention to voice, to decision, to what the author was trying to do and what the world they were in made possible.

The claim underlying this course is that code is writing. Not metaphorically. Writing is the technology of making thought visible, durable, and transmissible. Code does all of these things. The electricity is the part that makes it executable. Everything else — the decisions, the style, the accumulation of choices that adds up to a voice — is writing.

Reading code is a skill. It is not a talent. Every person who reads code well was, once, someone who could not. The skill is built by practice: by reading carefully, by reading slowly, by reading with a question in mind.

---

## Eleven codebases

| Unit | Title | What you will read |
|------|-------|-------------------|
| 01 | Early Unix | xv6, Research V6, Plan 9 |
| 02 | Classical Coding | tcc, GCC, vim, git |
| 03 | Richard Stallman | Emacs, GDB, Bison; the GNU Manifesto |
| 04 | Blender | The 3D creation suite; the community buyout |
| 05 | Culture, Spectacle and Eigenrank | TeX, BitTorrent, SageMath, Eigenrank |
| 06 | Languages and Theory | Assembly, LISP, Haskell; Church, Turing, Lovelace |
| 07 | The Mathematics Beneath | Mathlib, Agda; Grothendieck, Noether, Lawvere |
| 08 | Simplicial Homology | Building algebraic topology by hand, in code |
| 09 | Quake | The id Software arc; games as applied mathematics |
| 10 | TBD | |
| 11 | LLMs | nanoGPT; *Attention Is All You Need*; the horizon |

The course runs in order. Each unit uses the previous ones. By Unit 09 you will understand why Carmack's BSP tree is a cousin of the chain complex you built in Unit 08. By Unit 11 you will have a frame for understanding what it means to read code that produces language.

---

## Two tracks

**Track A — Classical**

Unix environment. Terminal navigation. vim or ed for editing. Compile the code yourself. The tools are part of the curriculum. Reading Carmack's renderer in a terminal, in vim, with the source opened in one pane and a running binary in another, is epistemically different from reading it in a modern IDE. The difference matters — not because the IDE is wrong, but because the tradition is real and inhabiting it changes what you understand.

Prerequisite: comfort at the terminal, or willingness to get there. The first two weeks serve as initiation for those who need it.

**Track B — Accompanied**

Any environment you bring. More scaffolding. More editorial guidance through the harder passages. You will not be thrown in without a guide.

Track B is honest about the tradeoff: something is lost when you are not in the tradition, and something is gained. The Track B student still learns that a tradition exists, what it looks like, and that they are now in relation to it — even if they do not inhabit it. That relationship is real and it matters.

**What both tracks share**

The course has a right way. Saying so is grounding and comforting regardless of which track you choose. Classical does not mean superior in a snobbish sense — it means there is a tradition, here is what it looks like, you are now in relation to it. Everyone is invited. No one is excluded from the ideas.

---

## How to read code

The hardest thing about reading a large codebase for the first time is not the complexity. It is the feeling that you should understand everything immediately — that if you don't, you are behind, or not ready, or in the wrong room.

You are not behind. You are not expected to understand everything. You are expected to orient yourself.

A few principles:

**Start at the entry point.** Every program starts somewhere — a `main()`, an `init()`, a kernel entry point. Find it. Read it. Then follow the calls. You are tracing a path through the code, not mapping the whole territory.

**Read for intention, not just function.** The question is not only *what does this do* but *why did someone write it this way?* What problem were they solving? What constraints were they working under? The comments, the variable names, the structure of the code all carry information about the thinking behind it.

**Accept confusion as part of the process.** You will encounter things you do not understand. Write them down. Come back to them. Often they become clear from context — from understanding the surrounding code — rather than from direct study.

**Use the history.** `git log`, `git blame`, the commit messages: these are evidence. The people who wrote this code left a record of their decisions. Read the record.

**Read alongside the primary sources.** Each unit is paired with documents that give the code context: Lions' Commentary for Unix, the GNU Manifesto for Unit 03, Turing's 1936 paper for Unit 06. The code and the writing illuminate each other. Read both.

---

## What you will have when it is over

You will have read eleven codebases. You will have met the people who wrote them — Ritchie, Linus, Stallman, Ton Roosendaal, Knuth, Lovelace, Turing, Grothendieck, Carmack. You will have followed a tradition from 1971 to the present day and seen how each piece grew from what came before.

You will know how to stand inside a large, unfamiliar codebase and find your bearings. You will know that this is a learnable skill. You will know that it is worth learning.

The final unit ends at the horizon: code that produces language, trained on the writing of everyone who has ever typed anything into a box and pressed send. We begin with Unix in 1972, when two people were trying to make a comfortable place to work. We end here.

The space between is eleven codebases, fifty years, and the whole story of how humans learned to write with electricity.

---

*Start with `01/`. The code is waiting.*
