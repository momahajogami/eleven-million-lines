# Brainstorm — 2026-08-04

## The Course Has a Personality

It's not a museum. It's curated with opinions. Knuth is a windbag AND TeX is a public performance AND it belongs in the course. That tension is the editorial voice. Fun, social, opinionated — but always in service of learning.

---

## Organizing Axes

- **Historical arc**: C compilers → Unix → networking → languages → tools
- **Code as performance**: TeX, Python, BitTorrent — written publicly and with pride
- **Skateboarding ethics**: Blender/Ton Roosendaal — gave up commercial product to go GPL, built a community, codes with joy
- **Built to tinker**: mupdf, Lua — small, readable, designed to be understood
- **Monastic/deliberate**: SQLite — the opposite of skateboarding, equally serious
- **Documentation as easter eggs**: stuff the repos with books, papers, .plan files, manifestos — things worth having, take them, they're yours

---

## Codebases and Characters

### Early Unix (01 — confirmed)
xv6 as the readable teaching version. At least a pair of repos — more than one Unix to explore. Lions' Commentary on Unix 6th Edition as paired text — literally written to teach people to read Unix source. Plan 9 also: Bell Labs trying again after Unix, Rob Pike and Ken Thompson, eerie elegance, different decisions.

### C Compilers (02 — confirmed)
DMR's original, PCC, tcc, early GCC. The tool that carved the world.

### Networking (candidate)
Ralph's admitted weakness — include it *because* of that. Early NCSA httpd, BSD sockets source. Stevens' *Unix Network Programming* as paired text. Where most people's understanding goes dark — that's exactly where the course should go.

### TeX
Not second, but in. Code as public performance. Knuth is a windbag — say so. TeX is overrated in some ways — say that too. But the literate programming idea, the obsessive correctness, the public pride of it — all worth teaching. Pair with the Gutenberg thread: movable type → early digital typesetting → TeX. A whole lecture on how humans have always engineered the distribution of text.

### Git
Early commits are tiny — Linus wrote the first version in two weeks, you can read the whole thing. The contrast between that and what it became is its own lesson about software growth.

### SQLite
Richard Hipp, largely alone, monastic and deliberate. More test code than source code. Runs on basically every device on earth. A different way to be serious.

### Quake / Carmack
The 1999 source drop was an act. Fast inverse square root, BSP trees — but also the attitude. His .plan files are a dev diary spanning years, incredibly readable. The repo plus the .plan files is a complete unit on how a mind works in public.

### BitTorrent / Bram Cohen
Charismatic, wrote about the art of coding with conviction. Protocol spec and reference implementation. Elegant protocol design as a teachable thing.

### Blender / Ton Roosendaal
Skateboarding ethics embodied. Gave up commercial software to go GPL. Built a community alongside the code. Pulls in: Audacity, GIMP/Glimpse, ImageMagick — a whole ecosystem of code written with joy and given away.

### mupdf
Open source and built to tinker. Small enough to read, serious enough to matter.

### Python / Guido van Rossum
Readability as a value, not an accident — the thesis is visible in the source. Early Python is clean enough to see the argument being made. Pair with his essays — he wrote a lot, thought out loud publicly.

### Perl / Larry Wall
Three virtues: laziness, impatience, hubris — meant seriously. Perl mirrors natural language, which is also gnarly. A counterpoint to Guido. Philosophy of expressiveness versus elegance.

### Haskell
In. Details TBD.

### Lisp / McCarthy
The 1960 paper is five pages and contains a complete programming language. Read it in an afternoon and feel the ground shift. Pair with a modern Lisp implementation. A unit on what ideas look like when first written down.

### Lua
Tiny, readable, designed to be embedded and understood. Built to tinker.

### Ruby / Matz
Designed for programmer happiness, said so explicitly, wrote about it in Japanese first. Cultural transmission from Japanese craft ethics into a programming language — real and underexplored. Connects to Ralph's Japanese studies.

### Perl / Larry Wall
Already listed above — but worth flagging as a strong counterpoint to Python in the same unit.

### zlib / Gailly and Adler
Invisible infrastructure made legible. Compression running silently inside almost everything. Written clearly and openly.

### OpenSSL — before and after Heartbleed
A unit on what happens when nobody reads the code.

### Aaron Swartz
RSS at 14, Reddit, Guerilla Open Access Manifesto. Code and writing together — a portrait of someone who believed information wanted to be free and paid for it. Ethics, law, politics, tragedy. Heavy but real.

### NASA / JPL
Code that flew spacecraft, now on GitHub. Mars rover code. Not elegant in the Carmack sense — *careful* in a way that makes you reconsider what software is for. Pair with mission documents. What does it mean to write code where a bug kills people?

### Forth / Charles Moore
Radically minimal. Almost a philosophy more than a language.

---

## Bell Labs as a Place

Deserves naming explicitly. Unix, C, Plan 9, AWK, grep, the transistor — one building in New Jersey for a few decades. Jon Gertner's *The Idea Factory* as paired text — reads like a novel. A Bell Labs week that cuts across multiple codebases.

---

## Characters Who Write About Code as Well as Write It

- **Brian Kernighan** — still alive, still writing. *The C Programming Language*, *The Unix Programming Environment*, *Understanding the Digital World*. Almost a syllabus by himself. Writes beautifully.
- **Carmack** — .plan files as dev diary
- **Guido** — essays and PEPs
- **Larry Wall** — manifestos
- **Bram Cohen** — conviction
- **Aaron Swartz** — Guerilla Open Access Manifesto
- **Knuth** — literate programming, windbag, worth it anyway

---

## The Physical and the Historical

Lions' Commentary was passed around as a photocopy for years — illegal to own, treasured anyway. Code as samizdat. That history belongs in the room. The scarcity and then the opening.

This course stuffed with easter egg PDFs is doing something similar: here, this is worth having, take it, it's yours.

---

## The Gutenberg Thread

One slot — or one lecture series — on how humans have always engineered the distribution of text. Movable type → early digital typesetting → TeX. Connects to Ralph's lifelong interrogation of reading: shorthand, Japanese, Spencerian, the history of writing.

---

## What the Course Is Secretly About

Every codebase was written by someone who thought they were solving a specific problem and accidentally wrote something that lasted. McCarthy wasn't trying to found AI. Knuth wasn't trying to define typesetting forever. Torvalds wasn't trying to replace Unix. They were just trying to finish something.

That might be the first lecture. And the last one.

---

## The Social Layer

The skateboarding ethics crowd — Blender, GIMP — built *communities* alongside code. No CS course teaches that alongside the code itself. This one should.

Fun and social means: opinions in the editorial content, easter eggs in the repos, history in the room, and the feeling that you are joining something when you read these codebases — not just studying them.

---

## Two Tracks

The course has a point of view — and says so on day one. Most courses pretend neutrality. This one doesn't. That's part of what makes it memorable.

**Track A — Classical**: Unix environment, vim or ed, command line navigation, compile it yourself. The tools are part of the curriculum. Reading Carmack's code in a terminal with vim is not the same course as reading it in VS Code with IntelliSense — it's epistemically different. This is initiation, not hazing. Initiation connects you to something real.

**Track B — Accompanied**: Any environment the student brings. More scaffolding. Honest about the tradeoff. The Track B student who does the whole course in VS Code still knows: there is another way, people have done it that way for fifty years, I could find my way there if I wanted. That knowledge changes how they hold their tools — less assumption, more awareness.

**What both tracks share**: The course establishes that there is a right way. Saying so is grounding and comforting regardless of which track you choose. Everyone is invited. No one is excluded. Classical doesn't mean superior — it means there is a tradition, here is what it looks like, you are now in relation to it.

**Possible structure**: First two weeks are the classical environment itself — not optional, not graded hard, but required as orientation. By week three you're reading Lions' Commentary in vim in a terminal and it feels right because you've been living there.

---

## Moods and Landscapes

Each unit has an atmosphere. Not just a codebase and a paired text — a world the student has to feel before they can understand what was built in it.

### Bell Labs, 1972 — The Modest Palace

*In 1972, things were typically well made. People at times felt like they were breaking convention, but the conventions were there like solid ground beneath you. No big international supply chains. Not a ton of plastic or electronics. Life was beautiful and rich and aesthetic and there was nowhere, not even New Jersey, that was totally distant from nature. It was a moment carved out for this — this prose, or call it what you will. It was a modest palace built to host for a few decades the life of the mind, and great things were accomplished.*

This is the opening of the Bell Labs unit — in Ralph's voice, kept as written. The code that came out of Bell Labs is inseparable from the world that produced it. Unix is not just a technical achievement — it's an artifact of a particular moment when people believed you could build things that lasted, when craftsmanship was still the default, when a working class job and a life of the mind were not considered opposites.

And what was discovered there: that you *could* code. That the ladder of bootstrapping could reach anywhere. That language could build language. That was not obvious. It had to be discovered by specific people in a specific building in New Jersey who went home at night to a world that still had weight and texture — and didn't yet know what it had made.

### Stallman's Media Lab, late 1980s–1990s — Righteous and Sleepless

One man's war. Fluorescent lights at 3am. Sleeping under the desk. The GNU Manifesto as a moral document, not a business plan. The last moment when refusal felt like enough — when one person could hold the whole system in their head and say: no, this will not be enclosed.

### id Software, 1993 — Fast, Loud, Shipping

Texan. Getting Doom out for Christmas. Carmack thinking in public via .plan files. The source drop as an act of faith in the community. Speed and craft as the same thing.

### Blender / Amsterdam — Open and Given Away

Ton Roosendaal handing the whole thing to the community. The GPL as a gift. Code built with joy, maintained with joy, taught with joy. The skateboarding mood at its most fully realized.

### The Competitive Programmer at 2am — Alone and Sharp

A different kind of code life. Solitary, optimized, in a particular flow state. And then the best ones become the most generous teachers — Petr Mitrichev, Tourist — because they understand that knowing how is only interesting if someone else can learn it.

### Cryptonomicon — The Romance of Deep Competence

Neal Stephenson writing about men who think in systems. The mood of finding the world more legible when it has structure. A love letter to a certain kind of mind — worth examining honestly. Is it healthy? Is it a way of loving the world? The course can hold the question without answering it.

---

## The Formal Languages — Category Theory Thread

Agda: the code *is* the argument. Reading Agda is reading mathematics being made rigorous in real time. Pair with Lawvere's *Conceptual Mathematics* — the most humane introduction to category theory ever written. The unit: here is an idea precise enough to be executed, here is the most beautiful way to explain it.

Sage and GAP: the working mathematician's tools. Not elegant in the literary sense — workbenches, accumulated, collaborative. This is what mathematics looks like when it's being done rather than displayed. Sage in particular is a massive codebase wrapping decades of mathematical software — PARI, FLINT, GAP itself — all unified under Python. Reading it is reading the sociology of mathematical computation: who built what, when, for whom, and how it got glued together. GAP is older and stranger, a language designed by group theorists for group theorists, with its own syntax and its own culture. Neither is pretty. Both are alive. A unit on Sage and GAP is a unit on what it looks like when mathematicians are the users and the authors — not engineers solving a business problem, but people trying to think. The paired text writes itself: a paper that used Sage to prove something, the code that produced the result sitting right there in the repo. Mathematics made reproducible. That's not a small thing.

The category theory thread connects: Haskell, Agda, Lawvere, MacLane — and underneath it all the Curry-Howard correspondence. Types as propositions. Programs as proofs. A unit that could change how a student sees both mathematics and software forever.

---

## The LLM Unit

Early transformer code. *Attention Is All You Need* — the paper and the original implementation. Small enough to read. Recent enough that students have a lived relationship with what it produced. Strange enough that the gap between the elegant simplicity of the mechanism and the enormity of what emerged raises exactly the questions the course is built around.

What does it mean to read code that produces language? What does it mean that a language model can now read code? The course holds that question without answering it.

The existential crisis AI has triggered is not a problem for the course — it is the audience. Everyone who loves coding is asking what it means. Everyone who has ever been curious about technology feels suddenly invited. The LLM moment didn't create this course. It created its moment.

---

## Style Is Ethics — The Explicit Argument

Nobody makes this argument clearly enough: the way you write code is a moral act. Not because of what the code does — because of what it says about how you think about the people who will read it after you.

- Knuth writing literate programs: *I think you deserve an explanation*
- Carmack dropping source: *I think you can handle this*
- Heartbleed: *I didn't think about you at all*

Skateboarding makes this explicit: you learn in public, fall in public, share what you figured out because the point is not to have the trick — it's to do the trick. The spot belongs to everyone.

A repo on contest coding is where the course makes this connection explicit. Competitive programming sits in tension with skateboarding ethics — individualist, secretive, optimized for narrow performance. But the best competitive programmers become the most generous teachers. Style and ethics are not separate categories. How you code is how you think about other people.

---

## The Missing Voices

Almost everything named so far is white men from America or Europe. That's partly the history — Bell Labs, MIT, Stanford in those decades were what they were. Worth being honest about and actively countering where possible.

- Yukihiro Matz — Ruby, Japanese craft ethics in a programming language
- Audrey Tang — Perl, public service, Taiwan
- Who else? An open question worth sitting with — not to fill a quota, but to find the people whose code genuinely belongs here and who get left out of the usual canon

---

## The Notebook Tradition

Mathematicians keep notebooks. Ramanujan's were found after his death — still being worked through. Darwin's. Leonardo's. The notebook is where thinking happens before it becomes argument.

Dijkstra wrote everything by hand — his EWDs, thousands of them, scanned and online, free. Reading a Dijkstra EWD is reading a mind being precise in public. No wasted words. No softening. Here is what I think and here is why and I will not apologize for the difficulty. That's a kind of writing almost nobody does anymore. The editorial content in each repo could be written in that spirit — short, precise, opinionated, signed.

Dijkstra insisted on handwriting because it slowed him down productively — forced him to think before committing. Knuth typeset his own books because the relationship between thought and its physical presentation mattered to him. These are positions about cognition, not eccentric habits. Connects directly to Ralph's practice: Spencerian, shorthand, the hand and the mind in relationship.

---

## Lockhart's Lament

Paul Lockhart's *A Mathematician's Lament* argues that mathematics education has destroyed the subject by turning it into procedures divorced from discovery. Students learn to execute algorithms without ever asking why, without ever feeling the pleasure of a problem.

The same thing has happened to coding education. Bootcamps, LeetCode, frameworks first. The act of programming — the thinking, the failing, the reading of what others have thought — stripped out.

This course is the answer to Lockhart's lament applied to code. The essay belongs in the syllabus. Maybe as the first reading. It is freely available.

---

## The Small Perfect Things

A unit on haiku. On the discipline of doing one thing and stopping.

- `diff` — compares two files. Does it perfectly.
- `cat` — concatenate files. One job.
- The Unix pipe — not a program, a philosophy made executable.

Most software today cannot stop. It grows, phones home, wants attention. These old tools are a rebuke to that. They still work and will work in fifty years. Held next to something like C++ — which nobody fully understands, which has accumulated decades of unwanted features — Forth asks the same question from a different angle: what are you actually trying to say? What is the minimum notation for this thought?

Forth is Walden written in concatenative stack-based code. Charles Moore designed it to be implementable by one person, on any hardware, in a weekend. That was the constraint and the philosophy.

---

## The Oral Tradition

Dijkstra lectured without notes. Ken Thompson in interviews is laconic, precise, oracular. Ritchie was gentler. Carmack in talks goes deep fast and doesn't look back. These people have voices — not just writing voices, speaking voices. The course should include recordings. Let students hear what it sounds like when someone thinks this way.

---

## The Course as a Room

Every time the course has been described, it's imagined as a room. A classroom in Ohio. Students opening a file. The ground shifting. That's not incidental — the course is a physical gathering. People in a place, together, with the same text open. What lectures were before they became content delivery. What Bell Labs was — a building where people ran into each other in the hallway and argued.

The long game: create the conditions where something like Bell Labs could happen again. Small. Intentional. Full of people who read.

---

## Document Tiers — What Goes in the Repo

### Tier 1 — Include Freely
Public domain and permissively licensed. Stuff the repos with these:
- Dijkstra's EWDs — scanned, free, online
- The original Unix paper (Ritchie & Thompson, 1974)
- The GNU Manifesto
- The GPL itself — read as a legal poem
- Carmack's .plan files
- RFC documents — RFC 793 (TCP), RFC 2616 (HTTP), public domain, beautifully written; the networking unit could start here before any codebase
- Early ACM papers out of copyright
- McCarthy's 1960 Lisp paper
- *Attention Is All You Need* — arXiv, free
- Lockhart's *A Mathematician's Lament* — free PDF, widely shared with author's blessing
- Stallman's essays
- Bell System Technical Journal issues — many now public domain
- Project Gutenberg texts for literary pairings
- Knuth's early papers (some free)

### Tier 2 — Link and Excerpt
Copyrighted but excerptable under fair use for educational purposes. A key passage, a defining paragraph — enough to taste. Then citation and link.
- *Conceptual Mathematics* (Lawvere) — one defining page
- *The Art of Computer Programming* (Knuth) — a famous passage
- *The Idea Factory* (Gertner) — the Bell Labs atmosphere paragraph
- *Cryptonomicon* (Stephenson) — the relevant scene
- *A Mathematician's Lament* (Lockhart) — free but worth noting
- *Extra Lives* (Bissell) — for the Quake unit
- Stevens' *Unix Network Programming* — a key chapter opening

### Tier 3 — Reading List Only
Books students should own or find. Each entry gets a one-paragraph argument for why — not a dry bibliography but a case made. That annotation is itself course content.
- *The Art of Computer Programming* — Knuth
- *Conceptual Mathematics* — Lawvere & Schanuel
- *The Idea Factory* — Gertner
- *Categories for the Working Mathematician* — MacLane
- *Types and Programming Languages* — Pierce
- *The Unix Programming Environment* — Kernighan & Pike
- *Hackers* — Levy (the social history of the culture)
- *Cryptonomicon* — Stephenson (fiction that earns its place)
- *Civil Disobedience* — Thoreau (for the Swartz unit)

---

## Open Questions

- How many repos per slot? At least a pair for Unix — why not elsewhere too?
- What is the structure of a unit? Lectures, exercises, paired readings?
- Who is the audience — undergraduates, graduates, working programmers, all three?
- Which slot for networking? Which for the Lispers?
- Is there a slot for the humanities thread (Gutenberg → TeX) as its own unit?
- Where does Aaron Swartz go — ethics unit, or woven throughout?
- How do we handle OpenSSL/Heartbleed — cautionary tale, or a full unit on reading for security?
