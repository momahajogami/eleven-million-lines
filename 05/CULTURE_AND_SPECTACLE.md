# Unit 05: Culture, Spectacle and Eigenrank

*No one knows what coding is. That is not a failure of definition. It is the most interesting fact about it.*

---

## The thesis

We have been building toward something.

Unit 01 showed you the ground floor: a working operating system, small enough to hold in your mind, old enough to be the origin of nearly everything. Unit 02 showed you how the ground floor gets made: the compiler, the tool that translates human intention into machine instruction. Unit 03 showed you the person who looked at those tools and decided they had to be free — and built the legal and technical infrastructure that made "free" enforceable. Unit 04 showed you what happens when that infrastructure is used not to write systems code but to make something beautiful: a 3D tool built by a community of artists, freed by collective purchase, sustained by people who believed the tool should belong to everyone who used it.

Now we are going to stand back and ask a question that none of those units asked directly: **what is this thing we have been doing?**

The answer this unit proposes: *coding is writing augmented with electricity.*

Not metaphorically. Not as a comparison. Writing is the technology of making thought visible and durable and transmissible. Code does all of these things — it makes logic visible, makes it durable (a program written in 1971 can still run), and makes it transmissible (you can copy it, share it, fork it, translate it). The electricity is the part that makes it executable — that makes the writing do something beyond being read.

This matters because it means code has a culture in the same way writing has a culture. It has styles, schools, debates, traditions, venerated texts, bad habits, living masters, and dead ones whose influence persists. The history of code is, among other things, a history of writing — and like the history of writing, it is storied and character-driven and full of people who cared desperately about things that looked, from the outside, like they did not matter.

This unit is about six of those stories.

---

## On style

Before the projects: a word on style, because this unit insists on it.

In skateboarding — as in jazz, as in calligraphy, as in any practice where skill is learned in public and transmitted through imitation and variation — style is not decoration. It is information. Two skaters can execute the same trick. One looks like themselves doing it. The other looks like everyone. The difference is not difficulty. It is commitment, economy, signature — the accumulation of ten thousand small decisions that add up to a way of doing the thing.

Code has style in exactly this sense. You can read Knuth's TeX source and know it is Knuth's — the mathematical elegance, the obsessive completeness, the self-documenting structure, the willingness to solve the right problem instead of the convenient one. You can read Bram Cohen's BitTorrent protocol specification and know it is his — the directness, the absence of ceremony, the impatience with anything that doesn't serve the protocol's purpose.

Style is not personality imposed on a technical artifact. Style is what technical decisions look like when they are made by someone who has thought deeply about what they are doing. The decisions accumulate. They become recognizable.

This unit pays attention to style. Not to evaluate it, but to see it — to read code and documentation the way you would read prose, asking not just *what does this do* but *what kind of mind made this, and why did they make it this way?*

---

## Interlude: The skateboarding parallel

Skateboarding emerged in the late 1950s from surfing culture in California — what surfers called "sidewalk surfing" when the ocean was flat. For twenty years it was a toy. Then in 1975 and 1976, the empty swimming pools of drought-stricken California became the venue for something new: vertical skating, the transition from flat ground to curved surface, gravity as a collaborator instead of an obstacle.

The culture that built up around this was self-organizing in a way that has no corporate equivalent. There was no institution that decided which tricks were valid. There was no authority that certified a skater as professional. There was the community — the other skaters at the spot, the readers of *Thrasher*, the people who watched the videos. The community decided what counted. The community remembered who did it first. The community enforced a norm against kooks and posers that was informal, unwritten, and absolute.

The code of that culture:

**You learn from watching.** The transmission of technique in skateboarding is almost entirely visual. You watch someone better than you until you can feel what they're doing, then you try it until your body knows it. The videos are the curriculum. The magazines are the canon.

**You contribute to the spots you use.** A good skate spot is public infrastructure used in a way it wasn't designed for. The skaters who use it clean it, wax the ledges, tell other skaters about it. They maintain it without owning it.

**Style is judged but not taught.** You can learn tricks from anyone. Style comes from living in the culture long enough that your decisions accumulate into a recognizable voice. No one can give it to you. The community knows when it's there.

**The trick belongs to the person who invented it.** This is the intellectual property norm of a culture with no formal intellectual property. Everyone knows who landed the first 900 — Tony Hawk, 1999, at the X Games, after years of failed attempts. Everyone knows who invented the kickflip. The priority matters. The credit is real. The knowledge is free — you can copy the trick, you can try to do it better, you can build on it — but the inventor's name stays attached.

These are also the norms of open source software, arrived at independently by a different community making different things in public.

Watch the parallel as each project's story unfolds.

---

## The projects

### TeX — *The document as proof*

In 1977, Donald Knuth received the galleys for the second volume of *The Art of Computer Programming* and found them ugly. The craft of mathematical typesetting, which had produced the first volume's beautiful pages through decades of hot-metal type, had been replaced by phototypesetting that Knuth found aesthetically intolerable. He stopped. He decided to build his own typesetting system.

He estimated it would take six months. It took ten years. He named the system TeX (from the Greek τέχνη, *techne* — art, craft, skill). He named the font system Metafont. He wrote a typesetting program and a font-rendering program from first principles, in a language he invented (WEB — literate programming, where code and documentation are the same document, readable as a book).

The TeX source — `tex.web` — is one of the most carefully written programs in existence. Knuth numbered every change to it. Version 3.0 was declared essentially complete in 1989. After that, the version number began converging toward π. The current version is 3.141592653. When Knuth dies, it will be set to π exactly and frozen forever. This is the statement of a craftsman: the work is done. Further revision would not improve it; it would change it. The pot is fired.

TeX is the standard for mathematical and scientific publishing worldwide. Every paper in physics, mathematics, and most of computer science is written in it. The arXiv — the open repository where most of those papers live before (and often instead of) journal publication — runs TeX. The document you read when you read a theorem is the output of a program written because someone found ugly typesetting intolerable, in the same way that skateboarding began because someone found the ocean flat.

Leslie Lamport built LaTeX on top of TeX in 1984 — macros that gave TeX a document structure: sections, citations, figures, cross-references. LaTeX is to TeX as a house is to lumber.

**Style note:** Read the TeX source (in `05/latex2e/` or the WEB file in `05/scratch/`). Knuth's code is like his prose: dense, elegant, thorough, and written as if the reader deserves the full argument. He does not optimize for brevity. He optimizes for correctness and for the reader's understanding. This is a specific style commitment that shows up in every line.

**The skateboarding read:** Knuth invented TeX and then gave it a version number that converges to π. He named the changes. He assigned priority. The intellectual credit is precise and permanent, the way trick priority is precise and permanent in skateboarding. And the knowledge is free — TeX is open, the WEB source is public, anyone can read the program the way they read the math it typsets.

---

### BitTorrent — *The network as commons*

Bram Cohen is a programmer from New York who in 2001 was thinking about the problem of file distribution: how do you get a large file — a Linux distribution, a movie, a game — to a large number of people efficiently? The naive approach is a central server. The server has the file. Everyone downloads from it. The server becomes the bottleneck. The more popular the file, the worse the bottleneck gets.

Cohen's insight: make the downloaders into distributors. Instead of getting the whole file from one server, break it into small pieces and get different pieces from different peers who are downloading the same thing. As you download pieces, upload the ones you have. The more people want the file, the more distributed the supply becomes. Popularity *helps* instead of hurting.

He wrote the BitTorrent protocol and released it in April 2001. He wrote the spec first — a plain text document describing exactly how the protocol worked — and posted it publicly before building anything. This is an important sequence: the idea was public before the implementation. Anyone could read it and build their own client. The protocol was never proprietary. It could not be made proprietary. Cohen understood that the value of a protocol is in its adoption, and adoption requires openness.

BitTorrent is now responsible for an estimated 20–30% of global internet traffic at any given time. It is the infrastructure for the distribution of open-source operating systems, independent films, academic datasets, public domain books, and (yes) copyrighted material downloaded without permission. The protocol does not know and does not care. The architecture is neutral. Cohen built a commons — a shared distribution infrastructure that belongs to no one and is available to everyone — and the commons has been used for everything.

The legal history is complex and ongoing. The BitTorrent protocol is legal. Some uses of it are not. The entities that have tried to restrict BitTorrent have consistently found that you cannot restrict a protocol — you can only restrict specific uses, and even that is difficult when the infrastructure is distributed. The network does not have an owner to sue.

**Style note:** Read Cohen's original BitTorrent spec (`05/scratch/bittorrent-spec.txt`). It is short — a few pages — and it is written in a register that is completely unlike Knuth's. Where Knuth is expansive and mathematical, Cohen is spare and functional. Every sentence earns its place. The elegance is in the compression. Two programmers, two problems, two styles — both right for what they were doing.

**The skateboarding read:** Cohen invented a trick and then made the trick public. Anyone can do it. The credit stays with him (the protocol is called BitTorrent; it is his name in the history). The trick spread because it was free to copy. The people who use it are not required to credit him, but they do — the name persists because the community keeps it.

---

### Linux — *The operating system as a letter*

We need to return to Linux, not because it belongs only here — its code belongs in the Unix tradition of Unit 01, its compiler in Unit 02, its license in Unit 03 — but because its story is the story of this unit told at maximum scale.

Linus Torvalds (see `02/LINUS.md` for his full character study) posted a message on a newsgroup in 1991. The message was casual, specific about what it wasn't (big, professional, GNU), and accurate about its ambitions (it resembled Minix; it probably wouldn't support anything beyond AT hard disks). The post was public. The code was public from the first release. The development process — the patches, the arguments, the version numbers — was public and remains public today on the Linux Kernel Mailing List.

What grew from that message is now the largest collaborative software project in history. More than 60,000 contributors. Over 27 million lines of code. The kernel that runs Android phones, internet servers, supercomputers, and spacecraft. Built in public. Maintained in public. Every commit visible. Every argument archived.

This is public spectacle in the most literal sense. The Linux kernel's development process has an audience of millions, a record that goes back thirty years, and no precedent in any other field.

The argument of this unit is that the publicness is not incidental to the quality. The kernel is good, in part, because its development is visible. Bugs get caught because eyes are on it. Performance regressions get caught because someone always notices. Design mistakes get debated because the debate is public and the person who says "this is wrong" can be answered in public, with evidence, by the person who made the decision. The accountability is structural.

The skateboarding parallel is most visible here: the Linux Kernel Mailing List is the spot. The spot has regulars. The regulars have norms. The norms are enforced by the regulars. Someone new who shows up with bad patches gets feedback that is sometimes brutal. The standard is high because the stakes are high — the kernel runs things that matter.

---

### SageMath — *Mathematics as a right*

William Stein was a mathematician at the University of Washington who was tired of recommending expensive proprietary software to students. In 2005, the tools for serious mathematical computing — Mathematica, Maple, MATLAB, Magma — cost thousands of dollars per license. Graduate students couldn't afford them. Researchers in developing countries couldn't afford them. High school students who wanted to explore serious mathematics couldn't afford them.

His response was SageMath: a free, open-source mathematics system built on Python, unifying the best existing free mathematical libraries — NumPy, Matplotlib, SymPy, GAP, R, and dozens more — under one interface. Not building everything from scratch. Building the roof over a house whose walls were already standing.

The mission statement he wrote is worth reading in full. He named the four M's — Mathematica, Maple, MATLAB, Magma — and said explicitly: this is the competition. Not in terms of commercial success, but in terms of capability. The goal was to make a tool so complete that a researcher who needed those tools would not need to choose between their mathematics and their ethics.

Stein later left his tenured position at UW to found CoCalc — a cloud-based mathematical computing platform that runs SageMath. The code is free; the service is a business. This is Ton Roosendaal's model applied to mathematics.

**The skateboarding read:** Stein built a new spot from materials lying around. The existing libraries — NumPy, SymPy, GAP — were already there, public, free, built by their own communities. Stein's contribution was to connect them and make the combination usable. This is the innovation pattern in skateboarding too: you don't always invent a new trick. Sometimes you find a new combination. Sometimes the innovation is in recognizing what's already there.

---

### SourceForge — *The repository as public square, and its betrayal*

Before GitHub, there was SourceForge.

In 1999, open source software existed in a scattered landscape: FTP servers, mailing list attachments, academic homepages that went dead when the researcher moved universities. SourceForge was the first platform to give open source projects a home that was public by design: version control, bug trackers, mailing lists, release hosting, all visible to anyone, all searchable.

At its peak, SourceForge hosted more than 300,000 open source projects. The projects in this course were SourceForge projects. GDB had a SourceForge page. GIMP had a SourceForge page. Early Blender releases were there. SourceForge was the place where the development of free software happened in public.

The second act is instructive and necessary.

In 2013, under new ownership, SourceForge began wrapping downloads of open-source projects — including projects whose maintainers had moved elsewhere and whose SourceForge pages were abandoned — in adware installers. The downloads included the software users wanted plus unwanted programs installed silently alongside it. The outrage was immediate and lasting. GIMP's project page was one of the ones wrapped. Projects fled. SourceForge's reputation did not recover.

What does it mean when the public square is betrayed by its landlord?

The projects survived. They moved to GitHub, GitLab, GNU Savannah, their own servers. The *code* is not lost, because the code is free — GPL-licensed code cannot be made proprietary no matter what the hosting platform does. But the community around the platform was disrupted. The history stored there (bug reports, mailing list archives, version histories) became untrustworthy.

This is the lesson that Stallman's GPL anticipated: the tools that hold the commons must themselves be held in common. A free license protects the code. It cannot protect the infrastructure that hosts the code. SourceForge is a data point in the ongoing argument about what "free software" means for infrastructure, not just source code.

The skateboarding parallel is direct: the spot gets skated out. The property owner posts a guard. The concrete gets knobbied. The spot you built your practice around closes. You move to a new spot. But you remember the old one, and you remember who closed it and how.

---

### Eigenrank — *The network as ballot*

Before there was a useful search engine, there were routes.

You followed links. Someone's home page linked to something they found interesting; that page linked to something else. The web was a set of paths, and you walked them. If someone linked to you, you were reachable. If no one did, you did not exist — not because you weren't there, but because there was no path to you.

Yahoo tried to organize this with a hand-curated directory: two graduate students at Stanford adding sites to a list by category. The web outgrew them in months. AltaVista tried full-text indexing: search by words. The result was a flood of pages that hid popular words in invisible text to game the rankings. Search became noise.

In 1996, Larry Page and Sergey Brin — also Stanford graduate students — started thinking about the web as a graph problem. Their insight: *a link is a vote, and not all votes are equal.* A link from a page that many people have linked to carries more trust than a link from a page no one has linked to. Trust propagates. The ranking of a page is determined not by the words on the page but by the collective judgment of the pages that point to it.

The mathematics requires solving an eigenvector equation. The ranking vector **r** is the dominant eigenvector of the web's link matrix — the steady-state distribution of a random surfer who clicks links with probability α and jumps randomly with probability (1 − α). The Perron-Frobenius theorem guarantees a unique positive solution. Power iteration finds it.

We call the algorithm **Eigenrank** because that is what it is. The name PageRank belongs to Larry Page and to a moment when Google's ranking was a relatively direct implementation of this eigenvector computation. That moment has passed. Google's current search layers machine learning over the original algorithm until the eigenvector is one signal among hundreds. Calling it Eigenrank names the mathematical discovery, which is ours to study; not the product, which has moved on.

Read `05/EIGENRANK.md` for the full account — the early internet, the Yahoo directory, the Geocities rooms with MIDI music and hit counters and hand-curated Cool Sites lists, and then the mathematics that made it possible to map all of it at once.

**The skateboarding read:** Brin and Page found a new spot — not a page on the web, but a way of *reading* the web's structure. They made the map public. The map changed the terrain it described: once pages were ranked by links, pages were built to attract links. The algorithm shaped the network it measured. The spot was transformed by the people who discovered it.

---

## What these six have in common

**They were public from the beginning.** Not released publicly after completion — developed publicly, with the community watching and sometimes participating. Linus posted his newsgroup message before Linux was finished. Cohen published the BitTorrent spec before the client. Knuth released TeX in stages and publicly numbered every bug fix. The publicness is not marketing. It is method.

**They have style.** Knuth's mathematical expansiveness. Cohen's functional compression. Stein's explicit mission statement. The Linux kernel mailing list's abrasive directness. These are not personalities imposed on neutral technical artifacts. These are technical artifacts shaped by the people who made them, in the way that a skater's tricks are shaped by the skater's body and practice.

**They changed something about what was possible.** TeX changed what mathematical publishing looks like. BitTorrent changed what distribution means. Linux changed what an operating system could be. SageMath changed who has access to mathematical computing. SourceForge changed what open source community looks like — and then, in its second act, demonstrated what losing that looks like.

**The beauty is caused by the publicness.** This is the argument. It is not provable in a strict sense. But the projects that emerged from this model — the elegance of TeX's output, the efficiency of BitTorrent's distribution, the power of the Linux kernel — are not coincidentally good. They are good, in part, because the making was public, which meant the community saw the work, responded to it, improved it, and held it to a standard that a private process does not generate.

---

## Connections

**From Unit 03:** The licenses that made these projects possible are Stallman's work. SageMath is GPL. Linux is GPL. GIMP is GPL. LaTeX uses the LaTeX Project Public License, designed on the same copyleft principles. SourceForge's failure is a case study in why license alone is not enough.

**From Unit 04:** Blender is this unit's immediate predecessor — a creative tool made in public, freed by collective action, sustained by a community. The open movies are this unit's spirit expressed in moving images.

**To Unit 06:** The arguments in this unit — about what code is, about writing and electricity, about style as information — lead directly into Unit 06's question: what are the languages this writing is written in, and where did they come from?

---

*Read the GNU Manifesto again. You read it in Unit 03 as a political document. Read it now as literature. Notice the style. Notice what Stallman chose to argue and what he chose to leave implicit. Notice the rhythm of the sentences. You are reading code's cousin — a document that encodes a logic, step by step, and asks the reader to execute it.*

*Then open* `05/scratch/` *and pick a starting point.*
