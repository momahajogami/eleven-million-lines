# Unit 05: Public Enterprise

*Code on display as art. Six projects. Six ways of being public. One argument: that software made in the open, for the commons, by communities rather than corporations, produces things that are genuinely beautiful — and that beauty is not incidental to the publicness. It is caused by it.*

---

## The theme

Every unit in this course has been, in some way, about who owns the tools. Unix: built in a corporate lab, eventually locked. C compilers: freed by Stallman's GPL. Blender: freed by a community fundraising campaign. Stallman's GNU: built specifically to create tools nobody could own.

This unit is about what happens *after* that question is settled in favor of the public. When the answer is already "nobody owns this — or everyone does" — what gets built?

Six answers. They are very different from each other. They share one quality: they were made in the open, by people who understood that making in public changes what you make.

---

## The projects

### LaTeX — *The document as art*

Donald Knuth was typesetting the second edition of *The Art of Computer Programming* in 1977 when he saw the galleys and found them ugly. Phototypesetting had replaced the hot-metal type he had admired in earlier editions, and the result was worse. He stopped. He decided to build his own typesetting system.

TeX took ten years. Version 3.0 was released in 1989. Knuth declared it essentially finished and began a tradition unique in software: he fixes bugs, but the version number converges toward π. The current version is 3.141592653. When Knuth dies, it will be set to π exactly, and frozen.

This is a statement about what the software is. It is not a product under development. It is a complete thing, like a poem or a proof. You do not continue to revise a poem after it is done.

Leslie Lamport built LaTeX on top of TeX in 1984 — a set of macros that gave TeX a document structure: sections, bibliographies, figures, cross-references. LaTeX is to TeX as a house is to lumber.

Together they are the standard for scientific and mathematical publishing worldwide. Every paper in physics, mathematics, and most of computer science is written in LaTeX. The source files for thousands of papers are publicly available on arXiv, which runs LaTeX under the hood. When you read a theorem, you are reading the output of a forty-year-old program that was built because someone found ugly typesetting intolerable.

The source code for TeX is written in a language called WEB — Knuth's own invention, a system for literate programming: the code and the documentation are the same document. You read the program the way you read a book.

**What this unit looks at:** the WEB source of TeX, the LaTeX2e kernel, and the concept of literate programming. The `.dtx` files in LaTeX packages are source + documentation interleaved — a direct descendant of Knuth's WEB idea.

---

### Glimpse / GIMP — *The image as commons*

GIMP — the GNU Image Manipulation Program — was written by Spencer Kimball and Peter Mattis as undergraduates at UC Berkeley in 1995. They wanted a free alternative to Photoshop. They released it under the GPL.

It is the first major application written for GNU/Linux. Before GIMP, the GNU project had tools — compilers, debuggers, shells — but not a creative application. GIMP was evidence that free software could be used not just to build tools but to make things.

GIMP's plugin architecture — a C API that lets anyone extend the program with new filters, import formats, and operations — is an expression of the same philosophy as Emacs's Lisp extensibility. The tool is designed to be incomplete. The community completes it.

**Glimpse** (2019–2022) was a fork of GIMP, created primarily to offer an alternative name and brand. It raised genuine questions about community, naming rights, and what it means to fork a project that is healthy. Glimpse is no longer actively maintained, but the questions it raised are not resolved. When is a fork the right answer? What does the community owe to the name?

These questions belong to this unit — not as technical problems but as political ones.

**What this unit looks at:** GIMP's plugin architecture, the Script-Fu scripting interface (Scheme-based, another Lisp), and the history of graphic tools in free software.

---

### Minecraft — *The world as folk art*

Minecraft is the outlier. It is not open source. Its source code is not public. Markus "Notch" Persson sold it to Microsoft in 2014 for $2.5 billion.

It belongs in this unit anyway, because the *making of it* was public enterprise in a different sense: Notch developed it in public, on forums, with the community watching and responding. Early versions were released for free or very cheap. The game grew from the outside in — players shaped it by playing it, reporting it, discussing it, making videos about it, building with it.

And then there is the modding community. Minecraft's code is closed, but the game was always designed — whether intentionally or by accident — to be modded. The modding community reverse-engineered the format, built tools, wrote frameworks, released thousands of mods under open licenses. A closed game generated an open ecosystem around it. The code was not shared, but the world was.

Minecraft is also the unit's argument in negative. By 2026, Microsoft's stewardship has produced a game that is safe, widely played, and commercially successful — and considerably less interesting than it was when Notch was building it on a forum with the community watching. The publicness was not just marketing. It was generative. When the development went private, something changed.

**What this unit looks at:** the history of Minecraft's development as public enterprise, the modding ecosystem (Forge, Fabric, and their open source codebases), and the argument about what happens when the commons is enclosed.

---

### SageMath — *Mathematics as commons*

William Stein was a mathematician at the University of Washington who was tired of recommending expensive proprietary software — Mathematica, Maple, MATLAB, Magma — to students and colleagues who couldn't afford it. In 2005 he started Sage (later SageMath): a free, open-source mathematics system built on Python.

The design choice: don't build a new system from scratch. Build a unified interface over the best existing free mathematical libraries — NumPy, Matplotlib, SymPy, GAP, R, and dozens of others — and make them talk to each other under one roof. The result is a system that can do symbolic algebra, numerical computation, graph theory, cryptography, and number theory from the same Python session.

The mission statement Stein wrote: *"Creating a viable free open source alternative to Magma, Maple, Mathematica and MATLAB."* The four M's. He was explicit about the target and explicit about why: not because proprietary software is bad engineering, but because mathematics is a public good, and the tools for doing mathematics should be available to anyone.

Stein's trajectory is part of the story: he left his tenured position at UW to build CoCalc, a cloud-based platform for mathematical computing that runs SageMath. His argument: the free software should be free; the service can be a business. This is Ton Roosendaal's model — "let the code be free and build professional services around it" — applied to mathematics.

**What this unit looks at:** SageMath's architecture (how it wraps and unifies dozens of free math libraries), its Python integration, and Stein's essays on mathematical software and freedom.

---

### SourceForge — *The repository as public square*

In 1999, most software existed in private, in corporate archives, or scattered across FTP servers and mailing lists. SourceForge changed this: a platform that hosted open source projects, gave them version control, bug trackers, mailing lists, and forums, and made the development process visible.

At its peak in the mid-2000s, SourceForge hosted more than 300,000 projects and was the center of open source culture. It was the place where code was public by default — not just the releases but the history, the bugs, the discussions, the arguments.

The projects in this course were SourceForge projects. GDB had a SourceForge page. GIMP had a SourceForge page. The early Blender releases were on SourceForge. Before GitHub, there was SourceForge, and before SourceForge, there was nothing like it.

The SourceForge story also has a second act, and the second act is instructive. In 2013, under new ownership, SourceForge began wrapping open source downloads in adware installers — silently adding unwanted software to downloads of projects the original authors had long since moved elsewhere. The community reacted with outrage. Projects fled. SourceForge's reputation did not recover.

What does it mean when the platform that hosts the commons betrays it? The projects survived — they moved to GitHub, GitLab, Savannah, their own servers. But the moment is a data point: the infrastructure of public enterprise is itself not immune to enclosure. The lesson is not despair. It is vigilance. And it is the argument for the GPL — for owning the platform, not renting it.

**What this unit looks at:** the history of SourceForge and what it built, the transition to GitHub (and what was lost and gained), and the question of infrastructure ownership.

---

### Pure Data — *The patch as performance*

Miller Puckette is a composer and computer music researcher who invented Max in 1986 at IRCAM in Paris — a visual programming language for real-time audio and MIDI processing. Max became a successful commercial product (Max/MSP, later Max 8, sold by Cycling '74). In 1996, Puckette created Pure Data (Pd) — a free, open-source reimplementation of the same ideas, released under a BSD-style license.

Pure Data is a visual language: programs are *patches*, networks of boxes connected by wires. The boxes are objects — oscillators, filters, delay lines, control logic. The wires carry signals — audio, control, MIDI, messages. A patch is a program, but it looks like a circuit diagram. When you run it, it makes sound.

This is a different relationship to code than any other project in this course. In Pure Data, the structure of the program is the interface. The patch *is* the documentation. There is no separation between the algorithm and its representation. A Pure Data patch for a reverb effect looks like, in some sense, a reverb effect.

Puckette chose freedom specifically. Max was successful and proprietary; Pd is free and has generated a community of musicians, artists, installation artists, and researchers who would not have existed without a free alternative. The community has extended Pd with hundreds of external libraries. The annual Pure Data convention is a conference where people perform with programs they have written and share the programs afterward.

This is code as art in the most direct sense: the program is performed. The audience hears the output. The program is available afterward to anyone who wants to understand or modify it.

**What this unit looks at:** the architecture of Pure Data (the audio graph, the message-passing system, the external object API), the history of live coding and algorithmic composition, and the tradition of art that publishes its source.

---

## What these six have in common

They are otherwise unlike. TeX is forty years old and frozen at π. Minecraft is closed source and corporate. Pure Data is performed live. SageMath is a Python library. SourceForge is a cautionary tale as much as a success story.

What they share:

**They were made in public.** The development process — the decisions, the arguments, the dead ends — was visible. This is not just a feature. It changes the thing being made. Software developed in public accumulates community. Community accumulates knowledge. Knowledge shows up in the thing.

**They were made for the commons.** Not all of them under the GPL, not all of them free in Stallman's strict sense, but all of them oriented toward a public rather than a paying customer. The design decisions reflect this. TeX is designed for reproducibility because reproducibility is what a scientific commons needs. SageMath is designed for pedagogy because mathematics education is a public good. Pure Data is designed for extension because the art community extending it is the point.

**The beauty is caused by the publicness.** This is the unit's core claim. TeX produces more beautiful mathematics than any proprietary typesetter. GIMP's plugin ecosystem contains things that no single company would have built. Pure Data has generated a body of musical work that commercial tools did not. SageMath can do things that no single proprietary tool can do, because it connects all the free tools together.

These are not coincidences. They are the argument.

---

## Connections

**From Unit 03 (Stallman):** The GPL licenses in this unit's projects descend from Stallman's work. GIMP is GPL. SageMath is GPL. Pd's BSD license is compatible. The legal infrastructure exists because Stallman built it.

**From Unit 04 (Blender):** Blender is in this unit's spirit — a creative tool made in public, for a public of artists. The open movies are what Pure Data performances aspire to: art that publishes its own source.

**Across the whole:** SourceForge hosted them all. GitHub hosts them now. The infrastructure of the commons is itself contested ground, and this unit's history of SourceForge is a reminder that the tools that hold the commons must also be held in common.

---

*Open* `commentary/vision.md` *for the extended frame. Then pick the project that interests you most and go there first.*
