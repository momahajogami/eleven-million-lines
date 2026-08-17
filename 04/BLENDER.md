# Unit 04: Blender

*The greatest all-around tool for editing shape. And a demonstration — maybe the clearest one in the history of software — that moral commitments and aesthetic ones are the same commitment.*

---

## A moment to stop and look back

Before we go further: look at what you have already done.

You have stood inside a working operating system — one small enough to hold in your mind, old enough to be the origin of almost everything. You have read `fork()`. You have traced the boot sequence of Unix. You have watched the kernel become reactive and wait.

You have read a compiler — two of them — and understood something about what it means for a program to read a program. You followed a C keyword from source text through tokenization, parsing, and code generation into machine instructions. You read the history of that process, from Grace Hopper's A-0 to Bellard's weekend contest entry. You modified a living compiler. Your name is in the version string.

If you walked away from this course right now, you would not walk away empty-handed. You would have what most programmers never have: a felt sense of the ground floor. The operating system. The compiler. The C language itself. The political and historical forces that shaped all of it. The names of the people who built it and why they built it the way they did.

That is real. That is yours. Hold it.

Now: keep going. Because the next unit is Blender, and Blender is extraordinary.

---

## What Blender is

Blender is a tool for editing shape.

That description is deliberately spare. Blender does many things — 3D modeling, rigging, animation, simulation, video editing, compositing, rendering, scripting — but all of it reduces to a single act: taking a description of space and transforming it. Moving vertices. Bending curves. Tracing rays of light through a scene. The diversity of Blender's features is not arbitrary accumulation; it is one idea expressed in many contexts.

Artists use it to model characters and environments. Architects use it to visualize buildings before they exist. Scientists use it to render molecular structures, fluid dynamics, astronomical data. Game developers use it as their primary asset pipeline. Animators use it to make films. The tool is genuinely general — not in the sense of doing everything badly, but in the sense of doing everything well enough that the same person can model, rig, animate, light, render, and composite without leaving the application.

Everyone who uses it seriously says the same thing eventually: it is the greatest tool of its kind. Not the most commercially successful — that would be Autodesk's suite. Not the one with the largest studio pedigree. The greatest. The most thoughtfully designed. The most honest about what it is.

That is not an accident. The design reflects the principles of the people who made it. The principles are worth understanding.

---

## Ton Roosendaal and the idea that held

Ton Roosendaal is a Dutch software developer and entrepreneur who founded NeoGeo in 1988, where Blender began as an in-house tool. In 1998 he founded Not a Number Technologies (NaN) to commercialize it. In 2002, NaN went bankrupt in the dot-com crash. Blender would have died with it — closed, inaccessible, the property of creditors who had no interest in 3D software.

Ton did something unusual. He went to the community of artists and developers who used the tool and asked: do you want this? And if you do, what will you pay for it?

The price was €100,000 — the amount required to buy the source code and IP from the bankruptcy estate and release it under the GPL. The community raised it in seven weeks.

On October 13, 2002, Blender became free software. The Blender Foundation was established to steward it. Ton has run it since. The source code has been public ever since.

Ton's operating principle, stated simply: *let the code be free, and build professional services around it.* The Foundation sells support, training, development contracts, and subscriptions to the Blender Studio platform. The code is never for sale because the code is never at risk. The freedom of the code is not a concession to the community — it is the condition that makes everything else possible.

This model has a name in the industry: open core, or sustainable open source. But Ton arrived at it not through business strategy but through a crisis. He needed the community to trust that the tool they were being asked to fund would remain theirs. The GPL was the only credible guarantee. He gave them the guarantee and they paid the price.

What makes this heroic is not that it worked. What makes it heroic is that it was right. The community was right to trust the guarantee. The GPL was the right instrument. Blender's thirty-year development since then — the growing team, the professional renders, the open movies, the millions of users — vindicates the decision completely.

---

## The moral and the aesthetic are the same thing

There is a question you could ask about any creative tool: why is it good?

For most tools, the answer is some combination of features, performance, and familiarity. Blender's answer is different, and it matters.

Blender is good, in significant part, because its internal representations are simple, open, and public. The file format is documented. The Python API exposes nearly everything. The node systems for shading, geometry, and compositing are built on the same architecture — learn one and you understand them all. The source code is available and readable. The development process is open to contributors.

These are not marketing claims. They are engineering decisions. And they have aesthetic consequences.

When the tool you are using to make something is honest about its own structure, you can learn it deeply. You can write scripts that automate the repetitive parts. You can understand why it does what it does. You can fix it when it is wrong. You can extend it when it is incomplete. The depth of understanding available to a Blender artist is qualitatively different from the depth available to a user of a proprietary tool, and that difference shows up in the work.

This is what it means for moral commitments and aesthetic ones to be the same commitment. Ton's insistence on freedom was not a sacrifice of engineering excellence for political principle. It was the recognition that openness *is* engineering excellence — that a tool built on principles of transparency and access will be a better tool, and that a community that trusts its tools will build better things with them.

The open movies are the proof. *Elephants Dream* (2006). *Big Buck Bunny* (2008). *Sintel* (2010). *Tears of Steel* (2012). *Cosmos Laundromat* (2015). Made by small teams. Made entirely with open source tools. Released under Creative Commons, freely available to anyone. They exist because Blender exists. They exist because the community paid to free it. And they are genuinely beautiful — not beautiful *for* open source films, but beautiful.

---

## The change in tempo

Units 01 and 02 were archaeological. You were excavating things that were built a long time ago — Unix in the early 1970s, C compilers from 1972 to 2001. The code had the authority of age. The people who wrote it were history. The machines it ran on were museum pieces.

This unit is different.

Blender is alive. It is being actively developed by a community of thousands. Ton is still working. The open movies are still being made. When you open the Blender source, you are opening something that was committed to this morning by someone in Amsterdam or Berlin or Seoul who cares about it.

The tempo changes. Instead of archaeology, what you are doing in this unit is closer to citizenship — learning the culture and principles of a living community, understanding where it came from and why, and then entering the conversation it is still having.

The political pressures you have been tracking through the previous units — the GPL, software freedom, the question of who owns the tools — are not historical here. They are present. Blender is the answer to those pressures, in real time, maintained by real people who made a real choice and keep making it every day.

That is worth something. Take your time with it.

---

## How to proceed

**Start by using Blender.** Download it from blender.org. Complete the Donut Tutorial by Andrew Price (Blender Guru) — it is the canonical introduction and it is genuinely good. Make something. It does not have to be impressive. You are doing this to have the experience of the tool, to understand what it feels like to model and light and render.

**Then read the story.** Ton's accounts of the 2002 campaign. The Blender Foundation's history. The production notes for one of the open movies. Lev Manovich on software as cultural form. Get the full picture of what Blender means before you read its code.

**Then open the source.** The commentary documents in `04/commentary/` will guide the walk — which files to enter, in what order, what the load-bearing ideas are. The DNA/RNA system. The dependency graph. The Python API layer. The render pipeline. These are worth reading, and they will read differently once you have used the tool and know the story.

---

## What this unit is arguing

Each unit in this course is making an implicit argument. For Unix: *this is where everything came from.* For the C compilers: *this is how everything is made.*

For Blender: *this is what it looks like when the principles hold.*

When Thompson and Ritchie built Unix, they were not thinking about software freedom — the concept barely existed. When Stallman built GCC, he was fighting for a principle that most people in the industry found eccentric. When Ton Roosendaal freed Blender, he was acting on thirty years of accumulated argument about what software should be — and the result was a tool that millions of people use to make things that are genuinely beautiful.

The argument of this unit is that those two facts are connected. The beauty and the freedom are not separate. The openness of the architecture and the quality of the output are not separate. Ton's slogan is not idealism dressed up as strategy. It is an accurate description of how good software gets made and stays good.

You are about to enter one of the most successful creative tools ever built. It was built this way on purpose. That purpose is worth understanding.

---

*Open Blender. Make something. Then come back.*
