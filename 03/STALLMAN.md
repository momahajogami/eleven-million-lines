# Unit 03: Richard Stallman

*The prophet. The printer. The four freedoms. The man who decided that the answer to the question "who owns the tools?" was: nobody. Everybody. You.*

---

## Where we are

You have read Unix — the operating system that gave programmers a common world. You have read the C compilers — the tools that made that world portable and reproducible. You have, in both cases, been standing inside code that changed everything.

Now we pause to meet the man who looked at all of that, saw what was at risk, and spent his life fighting for it.

Richard Matthew Stallman is not a peripheral figure in this course. He is its conscience. His ideas run underneath every unit — the GPL that saved Blender, the GCC you modified in Unit 02, the free software tradition that makes it possible to teach a course like this one at all. This unit brings him to the center, where he belongs.

---

## The printer

In 1980, at the MIT Artificial Intelligence Lab, the lab received a new Xerox laser printer. It was fast and capable, but it jammed frequently. On the old printer, Stallman had modified the driver to send a message to everyone waiting for their print job when the printer jammed — a practical, communal fix, the kind of thing that happened at the AI Lab as a matter of course. Source code was shared. Problems were fixed. That was the culture.

Xerox did not provide the source code for the new printer's driver. When Stallman learned that a graduate student at Carnegie Mellon had the source — Xerox had given it to them under a nondisclosure agreement — he asked for a copy. The student refused. He was bound by the NDA.

Stallman has described this as one of the most significant moments of his life. Not because of the printer. Because of what the refusal meant: that software could be used as an instrument of control. That the normal human impulse to help your neighbor — to share a fix, to pass on knowledge — could be made illegal by a license agreement. That the culture of the AI Lab, which had seemed like simply the right way to work, was fragile. It depended on people choosing to share. Companies were beginning to choose otherwise.

He decided to do something about it.

---

## The GNU Manifesto

In 1983, Stallman announced the GNU project on the net.unix-wizards and net.usenix newsgroups. His message was short and specific: he was going to write a free Unix-compatible operating system, and he needed help.

The name: **GNU's Not Unix**. A recursive acronym, a hacker joke, and a political statement in one. GNU would do everything Unix did. It would not be Unix. It would be free.

The GNU Manifesto, published in 1985, is the founding document of the free software movement. It is worth reading in full — it is available freely online and it reads with the directness of someone who has thought something through completely and is not interested in softening it for an audience that might disagree.

The core argument: software is knowledge. Knowledge wants to be shared. Preventing the sharing of software does not create value — it extracts value from the people who use the software and from the wider community who might improve it. The moral case for free software is not primarily economic. It is about what kind of world you want to live in. Do you want to live in a world where the tools you depend on can be taken from you? Where helping your neighbor is a license violation?

Read the Manifesto before you read the code.

---

## The four freedoms

Stallman defined free software with characteristic precision. "Free" does not mean "free of charge" — he was always careful to say "free as in freedom, not free as in beer." Free software is software that respects four specific freedoms:

**Freedom 0:** The freedom to run the program for any purpose.

**Freedom 1:** The freedom to study how the program works, and change it. *Access to the source code is a precondition.*

**Freedom 2:** The freedom to redistribute copies.

**Freedom 3:** The freedom to distribute copies of your modified versions to others.

These four freedoms are not aspirational. They are definitional. Software that does not give you all four is not free software, regardless of its price. This precision matters: "open source" can mean many things, some of which are compatible with proprietary elements. "Free software" in Stallman's sense has a specific, enforceable meaning.

The instrument of enforcement is the GPL.

---

## The GPL

The GNU General Public License is one of the most important legal documents of the twentieth century. Written by Stallman with help from lawyers at the Software Freedom Law Center, it uses copyright law against itself — instead of restricting what you can do with software, it restricts what *restrictions* you can place on it.

The mechanism is **copyleft**: if you distribute software under the GPL, any derivative work you distribute must also be distributed under the GPL. You cannot take GPL software, improve it, and sell it as a proprietary product. You cannot close the commons. The freedom is self-perpetuating.

Three versions:

**GPL v1 (1989)** — The original. Addressed the specific problem of proprietary distribution.

**GPL v2 (1991)** — Strengthened. Added the "liberty or death" clause: if you cannot distribute the software and comply with the GPL simultaneously (due to patent restrictions or other legal encumbrances), you cannot distribute it at all. The right answer to a conflict between freedom and a proprietary obligation is not compromise — it is refusal.

**GPL v3 (2007)** — Added protections against tivoization (distributing GPL software on hardware locked against modification), software patents, and DRM. Controversial in the Linux community; Torvalds has kept Linux on GPLv2.

The **LGPL** (Lesser GPL) allows proprietary software to link against free libraries without requiring the proprietary software to become GPL. A deliberate concession: Stallman wanted free libraries to be widely adopted, and requiring GPL compliance from every program that used them would have slowed adoption. The concession is calculated, not principled — he has written about why he prefers the LGPL only in specific strategic contexts.

---

## Emacs

Emacs began before GNU. Stallman wrote the first Emacs at MIT in the 1970s — a set of editing macros for the TECO editor, extended into something much larger. When he founded GNU, Emacs was the first project: GNU Emacs, 1985.

Emacs is an editor, but describing it as an editor is like describing a ship as a vehicle. Emacs is an environment — a Lisp machine disguised as a text editor. At its core is a Lisp interpreter. The entire editing experience — every command, every mode, every behavior — is implemented in Emacs Lisp and is therefore modifiable at runtime, while the editor is running. You can change Emacs while using it. You can program Emacs in Emacs.

This is the philosophy of Freedom 1 expressed in architecture. The tool is not a fixed artifact delivered to you complete. The tool is an environment you enter and participate in, changing it as you learn it.

For the forty years since its release, Emacs has accumulated layers: org-mode (an outliner, project management system, and literate programming environment), Magit (a Git interface widely considered better than any other), SLIME (a Common Lisp development environment), language servers, email clients, IRC clients, a psychiatrist (M-x doctor). The accumulation is not bloat. It is the natural result of giving millions of programmers a tool they can extend and sharing all extensions under the GPL.

The religious war between Emacs and vi users is the longest-running debate in computing. Both sides have a point. The vi tradition (Unit 01's ally) values minimalism, orthogonality, and doing one thing well. The Emacs tradition values extensibility, integration, and the editor as a world. The debate is not really about editors. It is about what a tool should be.

**What to look at:** The Lisp code in `emacs/lisp/` — over a million lines of it — is the living body of Emacs. Find `simple.el`. It is the simplest major foundation, and it is about 8,000 lines. Read it and feel the depth. Then read `scratch/doctor.el`. Then run `M-x doctor`.

**The surprise:** Stallman built a psychoanalyst into his text editor. `doctor.el` is his implementation of ELIZA — the 1966 Weizenbaum program that simulated a Rogerian therapist by reflecting user input back as questions. It has been in Emacs since the beginning. It is 1,654 lines of idiomatic Emacs Lisp from the 1980s, and it is playful, weird, and revealing. The person who wrote the GPL also wrote a program that asks you how you feel. Read `scratch/doctor-annotation.md` for context.

---

## GCC — revisited

You compiled code with GCC in Unit 02. You read its architecture. You understood it as a technical artifact: RTL intermediate representation, front-end/back-end separation, multi-language support.

Now read it as a political act.

Stallman started GCC in 1987 because a free operating system without a free compiler was not truly free. The compiler is infrastructure. If the compiler is proprietary, everything built with it is built on proprietary ground. GCC was not the best technical approach to building a compiler in 1987 — it was the necessary approach to building a *free* compiler that could compile a free operating system.

The GPL on GCC has teeth. When a company builds products using GCC and wants to modify it without releasing the changes, the GPL requires them to release. This has been enforced. The Free Software Foundation has litigated over GCC, over Busybox, over other GPL projects. The license is not decorative.

GCC also demonstrates the political dimension of technical choices. The early versions were slower and produced less optimized code than the proprietary compilers of the time. The goal was not to build the best compiler. The goal was to build a free compiler good enough that nobody would need a proprietary one. Over time, driven by the contributions of the community the GPL license created, GCC became one of the best compilers in existence. The political strategy and the technical quality are not separate.

---

## GDB

The GNU Debugger is less famous than GCC or Emacs but equally important to the GNU project's completeness. If you cannot debug your programs, you cannot develop serious software. A proprietary debugger in the middle of a free software stack would be a vulnerability — a place where the tool-user relationship breaks down.

GDB was written by Stallman in 1986 as part of the same logic. The GNU project needed: a compiler (GCC), an editor (Emacs), a debugger (GDB), an assembler (GAS), a linker (LD), a make replacement (GNU Make), a shell (Bash). Each one was a hole in the free software universe. Stallman and his collaborators filled them methodically.

GDB's architecture is worth studying: it communicates with running processes through ptrace, handles multiple architectures and binary formats, supports remote debugging over serial or network connections. It is the kind of infrastructure that becomes invisible when it works — which it has, reliably, for forty years.

**What to do in scratch/:** Write a small C program with a bug. Compile it with `-g` (debug symbols). Run it under GDB. Set a breakpoint. Step through execution. Read the registers. This is the experience that GDB was built to provide, and it is direct evidence of why the GNU project's completeness mattered.

---

## The connections

**From Unit 01 (Unix):** GNU is defined in opposition to Unix — its name says so. The AI Lab culture that Stallman lived in was shaped by the Unix tradition: tools that do one thing well, composable, sharing source. When AT&T locked Unix, Stallman's response was to rebuild everything. The connection is not just historical; it is structural. Unix gave the template. GNU gave the freedom.

**From Unit 02 (C compilers):** GCC appears there as a technical artifact and a political one simultaneously. Having read the code, you can now ask: what does it mean that this specific implementation — with its specific design choices, its GPLv3 license, its decades of community contribution — is the compiler that most of the world uses? The technical and the political are the same object.

**To Unit 04 (Blender):** The GPL that Ton Roosendaal used to free Blender in 2002 is Stallman's GPL. Without the legal instrument Stallman designed — without the specific mechanism of copyleft — the Blender buyout might not have been credible. The community paid because they trusted the license. They trusted the license because Stallman had spent twenty years building it, defending it, and explaining it. The thread runs directly.

**To Unit 05 (Public Enterprise):** Many of the projects in the next unit use GPL-compatible licenses. SageMath is GPL. GIMP/Glimpse is GPL. LaTeX is LPPL (similar in spirit). SourceForge was built to host GPL projects. The entire concept of "public enterprise" — code developed in public, for public benefit — owes its legal infrastructure to Stallman.

---

## The person

Stallman is a difficult person to write about because he is a difficult person. His technical contributions are unambiguous and enormous. His political contributions are equally large. His personal behavior has been controversial in ways that matter and have consequences.

This course does not resolve that tension. It acknowledges it. The ideas in this unit belong to the history of computing in a way that is independent of the person who originated them. The GPL would exist without Stallman. The concept of copyleft would exist without Stallman. The specific form they took — the specific legal argument, the specific language, the specific community — would not.

You are allowed to hold both things at once: that these are among the most important ideas in the history of software, and that the person who had them was complicated. Most important ideas come from complicated people. This is not an excuse. It is an observation about how history works.

Read the work. Form your own view of the person.

---

## Reading list

**Essential and free:**

- GNU Manifesto (1985) — gnu.org/gnu/manifesto.html. Read before anything else.
- "Free Software Is Even More Important Now" — Stallman (2013). gnu.org/philosophy/free-software-even-more-important.html
- GPL v2 and GPL v3 — gnu.org/licenses/. Read them as documents, not just as licenses.
- "Why Open Source Misses the Point of Free Software" — Stallman. The argument for why the distinction matters.

**On Emacs:**
- The Emacs manual — gnu.org/software/emacs/manual/. Freely available. The Emacs Lisp reference is the book that comes with the tool.

**Biographical:**
- *Free as in Freedom* — Sam Williams (2002). A biography of Stallman, revised by Stallman himself. Freely available under the GFDL at fsf.org.

---

## A note on the repositories

The primary source material for this unit is not a single repository but a constellation:

- **GNU Emacs** — in `emacs/` (blobless sparse checkout; `src/` and key Lisp files present)
- **GDB** — in `gdb/` (blobless sparse checkout; `gdb/` core present)
- **GNU Bison** — in `bison/` (blobless sparse checkout; `src/` present). Stallman wrote the first Bison as a replacement for yacc. Small repo, clean C, worth reading alongside GCC to see the compiler toolchain he assembled from scratch.
- **GCC** — already in `02/gcc/`; return to it with new eyes now that you know the political context
- **GNU Make** — not cloned, but worth knowing: Stallman wrote the first version in 1987. The source is at savannah.gnu.org/projects/make/. Like GDB and Bison, it filled a hole: a free operating system needs a free build system.

The `scratch/` directory is where engagement happens.

---

## What is in scratch/

**Primary FSF texts** — read these as documents, not just licenses:
- `gnu-manifesto.txt` — read first, before anything else
- `gpl-1.0.txt`, `gpl-2.0.txt`, `gpl-3.0.txt` — read them in order; notice what each version adds
- `lgpl-2.1.txt` — the strategic concession; read alongside the GPL to understand the difference between principle and strategy
- `free-software-definition.txt` — the four freedoms, formal
- `why-open-source-misses-the-point.txt` — the argument in concentrated form
- `free-software-even-more-important.txt` — the 2013 update; the landscape has changed, the argument has not
- `the-right-to-read.txt` — a 1997 short story; two pages; read it last; it will stay with you
- `gnu-coding-standards.txt` — Stallman's vision of how GNU code should be written; a technical document with a philosophical undercurrent

**The surprise:**
- `doctor.el` — Stallman's ELIZA implementation, built into Emacs since the 1980s. `M-x doctor`. Read `doctor-annotation.md` first.
- `doctor-annotation.md` — context for doctor.el: what ELIZA was, why Weizenbaum was disturbed by it, why it belongs in this unit

**Hands-on exercises:**
- `BUILD-emacs.md` — step-by-step: compile Emacs from `../emacs/` source; runs in 10–20 minutes on modern hardware
- `lisp-exercise.md` — modify a running Emacs without recompiling C; Freedom 1 in ten minutes
- `gdb-exercise.c` — a small C program with a deliberate bug; compile with `-g`, find the bug using GDB

---

*Open* `commentary/vision.md` *for the extended frame. Then read the GNU Manifesto. Then open* `scratch/` *and start a GDB session.*
