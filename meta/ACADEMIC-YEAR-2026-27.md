# Academic Year 2026–27
## Goals, Calendar, and Dreams

*Written 2026-08-29. Based on sessions 2026-08-18 through 2026-08-28b.*

---

## Where We Are Right Now

The website is live. The repo is public. Units 01–09 are seeded with commentary, codebases, and original course material. Units 10 and 11 are in active development. The September 2 publish deadline is in three days and we are effectively there.

The course has three simultaneous audiences, which is unusual and right:

1. **The center** — infants, toddlers, and preschoolers. The youngest learners. Families and caregivers alongside them.
2. **Horace Mann** — working with Kelly, 2026-27. The school program as a laboratory for what the course can be in practice.
3. **The course itself** — the full eleven-unit arc, for university students, adults, and families who want the whole thing.

These three are not separate programs. They are the same idea at different scales. What works at the center informs what works at Horace Mann. What works there informs what works in the course. The three run in parallel and teach each other.

**Note:** Return to Emerson in fall 2027 to work with Ina. See the fall 2027 section at the end of this document.

---

## The Academic Year Calendar

### September 2026 — Launch and Ground

**Course:**
- September 2: website live, repo public ✓ (effectively done)
- Announce on Hacker News, Lobste.rs, educator email lists
- Write `meta/ANNOUNCE.md` — the core announcement text
- Finish Unit 10 (Browsers and Social Media): codebase choices, BROWSERS.md, SOCIAL-MEDIA essays *(in progress this session)*
- Begin Unit 11 (LLMs): seed nanoGPT, download *Attention Is All You Need*, write UNIT-11.md

\*\*Horace Mann (Kelly):\*\*
- First session: what is a computer? What is code?
- Read something. Show how writing becomes behavior.
- No screens required yet. Paper, pencil, physical sorting games.
- Goal: establish that reading code is a form of reading, and they already know how to read.

**Center (infants, toddlers, preschoolers):**
- Meet families. Understand the rhythm of each age group.
- For infants: your presence is the curriculum. Read aloud. Show patterns.
- For toddlers: sequencing games. First this, then that. If/then in physical play.
- For preschoolers: the big question — what does a computer do? Can we make one with our hands?
- Begin sketching what a picture-book unit looks like. The website picture-book design (docs/index-picture-book.html) is the starting point.

---

### October 2026 — First Readings

**Course:**
- Unit 01 (Early Unix): finish `01/commentary/xv6/proc.md` — fork(), the scheduler. This has been pending since August 18. Write it this month.
- Unit 11: first draft complete — *Attention Is All You Need* reading guide, nanoGPT orientation, Stack Overflow arc
- Begin meta/pogrades/POGRADES.md — the partially-ordered grading system. Grading for a preschool-first course requires rethinking from scratch.

\*\*Horace Mann (Kelly):\*\*
- Second and third sessions: choose a first codebase together. Unit 09 (games) is the natural entry point — everyone has played a game.
- Look at Tetris source (09/other-games/tetris/tetris.py). It's 120 lines. Read it together.
- What does `rotate()` do? Can you trace through it with a pencil?
- Goal: one function, understood by the group.

**Center:**
- Preschoolers: introduce sequencing as a concept. Morning routine as an algorithm. Wake up → get dressed → eat breakfast → go to school. What happens if you change the order?
- Toddlers: pattern completion games. Red, blue, red, blue, ___? This is programming.
- Infants: music and rhythm. A repeating pattern with sound. This is a loop.
- Write one picture-book page this month. One. The hardest part is the first one.

---

### November 2026 — Depth

**Course:**
- Unit 07 (Grothendieck, topology): write `07/short_fiction.md` — Sesame Street-style character introductions. Grothendieck, Noether, Euler, Poincaré, Lawvere as characters with voices, not just names.
- Unit 07: write `07/LIBRARIES.md` — math libraries in C and Python as cultural expression
- Unit 03 (Stallman/GNU): begin writing the lecture arc — the story of the printer, the four freedoms, as a narrative for children and families
- All eleven units should have first-draft UNIT-N.md files by end of November

\*\*Horace Mann (Kelly):\*\*
- Go deeper on Tetris or pivot to a simpler codebase depending on the group.
- If the group is ready: look at initcode.S from xv6 — ten lines of assembly that start an operating system. Read it like a poem. You don't have to understand every word.
- Introduce the idea: old code, still running. The code that runs your computer was written by people, a long time ago, and it's still there.

**Center:**
- Preschoolers: a second picture-book page. This month: what is a loop? Wash your hands song as a loop. Row your boat as a loop. You've already been coding.
- Family night: invite parents for one evening session. Read a picture-book page together. Show the website. Let the children explain what they've been doing.
- Toddlers: binary choice games. Big or small? Hot or cold? This or that? Decision trees as physical play.

---

### December 2026 — Rest and Reflection

**Course:**
- No new units. Consolidate and rest.
- Rewrite CLAUDE.md Goals, Two Tracks, and Visualizations to fully reflect preschool-first framing. This has been pending since August 28.
- Read back through everything written. Find what's unclear. Note it but don't rewrite yet — let it rest.
- One thing: write the first draft of the course introduction. Not the website landing page — the actual document you'd give someone sitting down to take the course.

\*\*Horace Mann (Kelly):\*\*
- Holiday break. Before break: one session where the children tell *someone else* what they learned. A parent, a sibling, another teacher. Explaining is the test.
- Assign: over break, find one piece of code anywhere — a website, an app, anything — and bring back one question about it.

**Center:**
- Holiday rhythm. Read-alouds only. No new concepts. Consolidate relationships with families.
- Review what worked in October and November. What did the three-year-olds respond to? What landed flat?

---

### January 2027 — Language

**Course:**
- Unit 06 (Languages and Theory): fetch the McCarthy 1960 paper. Write the reading guide.
- Unit 06: write the Lovelace lecture — Note G as the first program. Who was she? What did she see that Babbage didn't?
- Begin drafting `meta/ANNOUNCE.md` v2 — a longer-form announcement for academic audiences (SIGCSE, education journals)

\*\*Horace Mann (Kelly):\*\*
- New semester energy. Introduce a second codebase: vim (02/vim). Not to use vim — to read what vim does.
- The question: what is an editor? How does an editor know where your cursor is?
- Pull up `src/normal.c` in vim's source. Find one function. Read its name. What does the name tell you?

**Center:**
- Preschoolers: introduce letters. A is for Algorithm. B is for Bug. C is for Code. Not to memorize — to play with. The alphabet as a kind of code.
- Write three more picture-book pages. Target by end of January: six pages total.
- Toddlers: sorting by attribute (color, size, shape) as categorization — the most fundamental operation in data structures.

---

### February 2027 — Story

**Course:**
- Unit 04 (Blender): write the narrative essay — the heroic story of the community buyout, what it means for software to be owned by its users
- Unit 05 (Culture and Spectacle): write the PageRank essay — Brin and Page as characters, the eigenvector as a way of seeing
- First session on Unit 10 with real students if the Emerson program is ready for it — browsers as a thing they use every day, now readable

\*\*Horace Mann (Kelly):\*\*
- The browser session. They use browsers every day. What is a browser?
- Show them BROWSERS.md. Not all of it — pick three paragraphs and read them together.
- Look at the Mosaic source (if cloned). Find the `<IMG>` tag implementation. This is the line that changed the web.

**Center:**
- Preschoolers: the picture-book draft is done enough to read aloud. Read it. Watch their faces. Notice what lands and what doesn't.
- Family night: second one. Bigger. Bring something visual — the website, the picture-book pages, something they can see.
- Infants: seven months of patterns, rhythm, cause and effect. They are learning. This is the foundation.

---

### March 2027 — Mathematics

**Course:**
- Unit 08 (Simplicial Homology): write the teaching version — how do you explain this to a parent and child sitting together?
- The Euler characteristic (-1 + 1 - 1 + 1 = 0 for the torus) as a picture-book moment. Count the vertices. Count the edges. Count the faces. Subtract, add, subtract. You get the same number every time.
- Write `07/hatcher/HATCHER.md` and download Hatcher PDF. Hatcher made the book free. Use it.

\*\*Horace Mann (Kelly):\*\*
- The mathematics session. Use Unit 08 directly — run `python examples.py` and look at what the homology groups say about the torus.
- Not the algebra. The pictures. Draw a torus on the board. Count holes. That's it.
- If one student asks why, follow the question wherever it goes.

**Center:**
- Preschoolers: counting and topology as the same thing. Count the holes in a donut (one). Count the holes in a pretzel (two). Count the holes in a ball (zero). You just did topology.
- Write the final picture-book pages. By end of March: complete first draft of a picture-book that stands on its own.

---

### April 2027 — Code and Community

**Course:**
- Unit 09 (Quake): seed the actual Quake source. Read Q_rsqrt. Write it on the whiteboard. Explain why the magic number is what it is.
- Decide: does Descent belong in 09? Make the call.
- Begin planning the first real teaching of the course — not an announcement, an actual class session, even informally.

\*\*Horace Mann (Kelly):\*\*
- Community session: the children share something they've read with their families.
- Not a presentation — a conversation. You read this. Tell me about it.
- The question: what do you want to read next?

**Center:**
- Picture-book complete and printed. One physical copy to hold.
- Share it with families. Get reactions. Revise.
- Begin thinking about what year two looks like.

---

### May 2027 — Review and Forward

**Course:**
- Every unit has a seeded codebase, a unit document, and at least one original essay.
- The website is updated with all 11 unit pages having real content.
- Write the end-of-year reflection: what worked, what didn't, what changed.

\*\*Horace Mann (Kelly):\*\*
- Last session: what did you learn? Not about code — about reading. Did it change how you read anything else?
- Document the year. What did they respond to? What was hard? What was surprising?

**Center:**
- End-of-year family gathering.
- The infants who were three months old in September are now nine months old. They have been learning through every session.
- The preschoolers who couldn't read in September may be reading now. Show them the picture book they helped make.

---

### June 2027 — Rest

Put it down. Let it be done for a month. Come back to it in July with fresh eyes and new questions.

---

## Dreams for Horace Mann (2026-27, with Kelly)

The Horace Mann program is the laboratory for 2026-27. It is where the course gets tested against actual children who did not choose to be there, who have had a full day of school, who would rather be outside. If it works there — if it holds attention, if it produces questions, if they come back the next week — it works anywhere.

The dream is simple: by the end of the year, there is at least one child at Horace Mann who looks at a website and thinks *I could read that*. Not who can read it — who thinks they could. The belief is the first thing. The skill follows.

A secondary dream: one of the parents gets curious. Asks to see the session notes. Reads a session log and recognizes something they learned once and forgot. The course works backwards through generations — children bring it home to adults.

The program does not need to be formal. It does not need a curriculum packet or a grading rubric. It needs one session per week, one codebase at a time, one question that is genuinely interesting, and someone willing to sit with the not-knowing long enough to find out.

---

## Fall 2027 — Return to Emerson (with Ina)

The 2026-27 year at Horace Mann is preparation. Fall 2027 is the return to Emerson, working with Ina.

By then there will be a full year of documented sessions, a tested reading list, a clearer sense of what lands with children and what doesn't. The work with Kelly will have produced evidence: what a unit looks like in practice, how long a codebase holds attention, which questions open things up and which close them down.

The Emerson program picks that up. Different school, different collaborator, same course — but a year wiser.

**What to bring from Horace Mann:**
- The session logs. What worked, what didn't, what surprised.
- The first codebase that genuinely held a room. Use it again. Let it be the foundation.
- The picture-book draft from the center, if complete. Read it on the first day.
- The questions that came up and weren't answered. Those are the curriculum.

**What to plan for fall 2027:**
- First session in September 2027: orient Ina to the course — the eleven units, the two tracks, the reading-not-programming argument.
- Choose a starting codebase together. Ina knows the students; defer to her on what will land.
- Establish the rhythm: one session per week, one file at a time, one question per session.
- By December 2027: one student has followed a piece of code from a file they opened to something they understand. That is the year's goal.

The return to Emerson is not starting over. It is the course finding another home.

---

## Dreams for the Center

The center is where it starts earliest. Infants, toddlers, preschoolers. They are not learning to code. They are learning the shape of systematic thinking — the shape that code later inhabits.

The dreams here are quieter and larger:

**For infants:** the understanding that patterns are interesting, that repetition is pleasurable, that a world that behaves consistently is a world worth exploring. You do not teach this. You embody it. Show up. Be consistent. Make the same sounds in the same order. Sing the same songs. The infant learns to expect the next note. That is prediction. That is the foundation of all modeling.

**For toddlers:** the first experience of making something that works. Stacking blocks in an order that doesn't fall. Finding the rule. Changing one thing and seeing what changes. This is science. This is programming. This is the kernel of everything.

**For preschoolers:** the picture book. A physical object they helped make, that they can hold, that has their fingerprints on it (literally and figuratively). Reading it to a younger sibling. Understanding that you can make things for other people to read. That is authorship. That is why we are here.

**For families:** a resource they didn't know existed. Not a class — a conversation. A reason to sit together with a book about code and feel that this is something they can participate in. That the tradition is theirs too. That their children are not behind, are not outside, are exactly where they need to be.

The picture-book draft lives in this document as a goal. By the end of the year there is a real picture-book: printed, bound, given to the children at the center. It begins: *A is for all of us.*

---

## What This Year Is For

Not to finish the course. The course will not be finished in one year. It will grow as long as there is something true to say about code and reading and the people who made the things we live inside.

This year is for beginning. Beginning in three places simultaneously — the center, the school, the course — so that they can teach each other. Beginning in public, with the website and the repo and the announcement, so that other people can find it and say *yes, this*.

Beginning so that next year, when the children at the center are a year older, there is already a year of work behind you.

That is enough for one year.

---
