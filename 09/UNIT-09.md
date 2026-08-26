# Unit 09 — Quake and the Grammar of Games

*The final level of any video game is coding.*

---

## The Central Argument

Writing requires four things: inner skill, interpersonal familiarity with the tradition, permission, and access to the technology. For most of human history, most people lacked at least one of these. Literacy was rationed. The printing press democratized reading before it democratized writing. The computer democratized the device before it democratized the skill.

Games are the most widespread form of this incomplete democratization. A game gives you the electronics but not the access. You hold the machine but you cannot speak to it — only listen. Gamification is a trade: physical access to the device in exchange for the mental experience of coding, the social inclusion in engineering and making. It gives you the feeling of agency inside a closed system.

This course exists because there is no necessary trade-off. Reading can be as engaging and satisfying as playing. The difference is that when you finish reading, you can write. When you finish coding, you can make worlds. The final level of any video game is the level editor. The final level of the level editor is coding. We are already there.

---

## Quake as the General Theme

Quake is the drama. The story has everything: two Johns, one engine, one game, and the implosion of one of the most creative partnerships in software history. Carmack building what the machine could do. Romero building what it felt like to be inside. The Christmas deadline. The source drop as an act of faith. The .plan files as public thinking.

But Quake is also the technical argument. It is applied topology, applied linear algebra, applied numerical methods — all under severe constraint, all shipped on a date certain. After Unit 07's pure abstraction and Unit 08's sandbox, Unit 09 asks: now build something real with it.

See also: `07/quake.md` — the bridge document situating Quake in the context of topology.

---

## The Repository and Its World

**Quake source** (id Software, GPL 1999) — the primary text. Read the renderer. Read the BSP code. Read `Q_rsqrt`. Read the entity system. Read QuakeC, the scripting language Carmack wrote so players could mod without touching the engine.

**Wolfenstein 3D source** (id Software, 1991) — the grandfather. Raycasting, not BSP. See how much changed in two years.

**DOOM source** (id Software, GPL 1997) — the bridge between Wolf3D and Quake. Where the id house style solidified. The WAD file format as a lesson in data-driven design.

**QuakeC** — the mod language. Team Fortress, Capture the Flag, Threewave CTF — all QuakeC mods. The community that grew around Quake is the open source community in miniature: people with the source, building things, giving them away, arguing about credit.

**Quake engine derivatives:**
- **GoldSrc** (Valve) — the Half-Life engine, Quake-derived. Counter-Strike, Team Fortress Classic. Valve's first move.
- **id Tech 3** (Quake 3 engine) — powers Jedi Knight II, Call of Duty 1. The engine that defined competitive FPS.
- **Darkplaces** — an open source Quake engine continuation, still maintained.

**Michael Abrash, *Graphics Programming Black Book*** — the technical companion text. Abrash was at id during Quake's development and wrote about it in real time. The best explanation of what the engine is doing and why. Free online.

**Carmack's .plan files** — dev diary spanning 1995–2000. Read them alongside the source. The code and the thinking-in-public, together.

**SDL (Simple DirectMedia Layer)** — what most Quake ports use to talk to the OS for input, audio, and display. A small, clean library that makes the engine portable. Worth reading on its own.

**OpenGL / glQuake** — the hardware-accelerated version. The original software renderer is more interesting educationally: Carmack doing by hand what GPUs now do automatically.

---

## The Access and Writing Thread

Hunt the Wumpus (1973) is literally text. Adventure (1976) is a conversation with a patient machine. Zork (1977) has a parser — a reader that responds in language. These are writing technologies, not games in the modern sense. The distinction between "game" and "text" was not yet obvious.

The transition from text → 2D sprite → 3D polygon is a story about writing evolving its medium. Gaining presence and immediacy, losing imagination and language. The reader's participation in the world's construction — which is total in a text adventure — narrows with each graphical step until, in a modern AAA game, it is nearly zero.

Coding reverses the direction. When you write code, you write a world. You restore the full access that games progressively withdrew. You become Miyamoto, not Mario.

The question this unit asks: when did games stop being a form of writing, and when did they start being a substitute for it? And what does it cost?

---

## Characters

**John Carmack** — the engine. First-principles thinker. Rebuilt the graphics pipeline three times because the previous solution was no longer interesting. Donated his share of id to charity. Now at Meta, working on VR. His .plan files are the best technical writing of the 1990s, posted without editing, free.

**John Romero** — the game. Built levels the way a novelist builds scenes. His split from Carmack after Quake is one of the great creative-partnership stories in software. *Daikatana* was the aftermath. He is still making games.

**Shigeru Miyamoto** — present in this unit as the writer. Mario and Zelda are spatial narratives. Miyamoto thought in levels the way a novelist thinks in chapters. He did not know he was writing. That is part of the argument.

**Roberta Williams** — Sierra On-Line, the graphic adventure. King's Quest, Space Quest. The person who brought pictures into text adventures, which started the long trade. Worth naming.

**Will Wright** — SimCity, The Sims. Games about systems, not stories. A different relationship to the machine — modeling, not narrating. The sandbox game before sandbox was a genre.

---

## What Coding and Games Have to Do With Writing

The question sounds rhetorical. It is not.

Writing is a technology. It requires: something to write with, something to write on, a tradition of symbols, someone who taught you, and permission to be in the room where writing happens. For most of human history, most people lacked permission. The symbol system was a guild secret.

The computer is the most powerful writing technology ever built. It is also, so far, the most successfully captured. We have given almost everyone a device and almost no one the skill to speak to it. We have built the most elaborate read-only system in history and called it access.

Games are the pleasantest version of this. They are beautifully designed read-only experiences. But the kid who plays ten thousand hours of Minecraft is not, thereby, a programmer — any more than ten thousand hours of reading makes you a novelist. Reading is necessary. It is not sufficient. At some point you have to pick up the pen.

This course is the pen.

---

## Intentions for this Unit

- Read the Quake source: renderer, BSP, entity system, QuakeC
- Read Wolfenstein 3D source alongside — see the evolution
- Read Abrash alongside the code
- Build something small with the Quake engine or a derivative
- Write `09/other-games/GAMES.md` — the full garden of games with histories
- Ask: what is the last level?
