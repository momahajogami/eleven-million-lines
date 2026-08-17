# Vision — Unit 05: What Public Enterprise Produces

*Six projects. One argument: that making in public is not just a distribution strategy. It is a design constraint. And design constraints produce beauty.*

---

## The argument, stated plainly

There is a widespread assumption in the software industry that quality requires secrecy. That the best tools are built by closed teams with proprietary incentives. That open development is a compromise — you give up some quality in exchange for some freedom.

This unit is a counterargument. Not an abstract one. Six concrete counterarguments, each a different shape.

TeX produces typography that proprietary typesetters have not matched in forty years. GIMP's plugin ecosystem contains algorithms that no commercial tool commissioned. Pure Data has generated a body of artistic work that commercial music software platforms did not. SageMath integrates mathematical capabilities that no single proprietary tool provides. Minecraft's modding community built a universe of free creative tools around a closed game. And SourceForge — before it betrayed its community — demonstrated that making the development process itself public changes what gets built and how.

The beauty is not despite the publicness. It is because of it.

---

## Three ways of being public

These six projects illustrate at least three distinct ways that software can be public enterprise.

**Public in source.** TeX, GIMP, SageMath, and Pure Data are open in the classical free software sense — source available, forkable, modifiable. The development history is visible, the decisions are documented, the community can participate. This is the form Stallman specified, the form the GPL protects.

**Public in development process.** Minecraft was never open source, but it was built in public: Notch developed it on forums, with the community watching and participating. Early versions were shared freely. The design decisions were made in dialogue with players. This is a different sense of public enterprise — not open source but open making. The code was closed; the process was open.

**Public as infrastructure.** SourceForge was public in a third sense: it was the *infrastructure* of public development. It did not write code; it hosted it. It made other projects' publicness possible. Its rise and fall illustrates the dependency of public enterprise on public infrastructure — and the vulnerability when that infrastructure is itself not public.

These three forms are in tension with each other. A project can be open source but developed in secret by a single company. A project can be developed in public dialogue with its community while remaining proprietary. An infrastructure platform can host open source projects while itself being closed and profit-driven. The distinctions matter.

---

## Literate programming and the document as source

Donald Knuth's concept of literate programming deserves its own moment here, because it connects to something deeper than just TeX.

Knuth's WEB system — the language in which TeX is written — treats the program and its documentation as the same artifact. You write a program as a document: prose explanations interwoven with code, structured for human reading. Tools then extract the code for compilation and the prose for typesetting. The human-readable document is the source of truth.

This is the inverse of the norm. In most software, the code is the source of truth and the documentation is added later, maintained separately, and allowed to drift. In WEB, you cannot have documentation that contradicts the code, because they are the same file.

The implications run through this unit. LaTeX documents embed their structure in markup. Pure Data patches are programs that look like what they do. SageMath notebooks interleave code and prose explanation (Jupyter notebooks, which SageMath uses, are a descendant of literate programming). These are different expressions of the same idea: that the program and its explanation should not be separated.

This idea is also the philosophical underpinning of the course you are reading. The commentary documents, the README files, the STALLMAN.md and BLENDER.md — these are an attempt to treat the code and the explanation of the code as a unified thing. We learned this from Knuth. He learned it from thinking carefully about what documentation was for.

---

## The Minecraft problem

Minecraft requires a longer look because it is the unit's most uncomfortable subject.

Minecraft was made in public and then enclosed. The community that formed around the public development — that shaped the game, modded it, built creative tools around it — is now building against a product owned by Microsoft. The modding community is technically in violation of the EULA. The Minecraft experience is administered by a corporation.

And yet: the modding community persists. Forge and Fabric are open source. The Minecraft community has produced creative work of remarkable variety and volume. Children have learned to program through Minecraft mods. Architects have built things in Minecraft that informed real buildings. The game, despite its enclosure, continues to generate public value.

What does this mean? Several things simultaneously.

It means that the creative energy of a public development process is not entirely lost when the software is enclosed — some of it survives in the community, in the mods, in the culture. It means that a game designed for play is inherently resistant to full enclosure, because the players will find ways to extend and share.

But it also means that the enclosure is real. The Minecraft of 2026 is not the Minecraft of 2011. The game that Microsoft sells is not the game that Notch built on a forum with the community watching. Something was lost when the development went private, and the community knows it even if it cannot fully name it.

The contrast with Blender (Unit 04) is instructive. Blender was also at risk of enclosure in 2002. The community's decision to pay to free it — to use the GPL as the instrument — produced a different outcome. Blender in 2026 is more open, more capable, and more community-developed than Blender in 2002. The trajectory bends in the opposite direction.

Minecraft is the unit's cautionary tale. Blender is its positive case. Together they make the argument: the GPL, or something like it, is not just idealism. It is the mechanism that keeps the trajectory bending toward the community.

---

## The mood

This unit is the most diverse in the course. It moves from the mathematical sublime of TeX to the political tragedy of SourceForge, from the geometric precision of Pure Data patches to the folk art of Minecraft builds. The student should feel the variety without losing the thread.

The thread: these are all things the commons produced. Not despite the publicness — because of it. The student's job is to feel that claim becoming more plausible as they move through the six projects, until by the end it is not a claim but an observation.

Then: look at Units 01 through 04 again. Unix. C compilers. Stallman. Blender. The commons has been producing the ground of computing for fifty years. It was always true. This unit is just where we stop and look at it directly.

---

## A reading for the unit

Yochai Benkler, "Coase's Penguin, or Linux and the Nature of the Firm" (2002). Freely available online. A law professor's argument for why large-scale open source collaboration is economically rational — why the commons produces things the market cannot. It is the academic version of the argument this unit makes through six stories.

Read it after you have engaged with the projects. It will make more sense.
