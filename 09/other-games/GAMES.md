# A Garden of Games

*Games are a form of writing. This is not a metaphor.*

Each game here is a text — written by someone who had something to say about space, time, consequence, and the reader's role. Some of them knew this. Most didn't. That's part of the story.

---

## Pong (Atari, 1972)

The same year as Unix. Dennis Ritchie was writing C at Bell Labs in New Jersey. Nolan Bushnell and Al Alcorn were building Pong in Sunnyvale, California. Two paddles. One ball. A score. The entirety of the game is approximately two hundred lines of hardware description — not software, hardware. The logic lives in transistors, not code.

Pong is not a story. It is a reflex. But it is the first time a machine invited a person to *respond*, and the person responded, and the machine responded back, and this felt like something new.

What it is: a two-way channel. Writing without words.

---

## Space Invaders (Taito, 1978)

Tomohiro Nishikado built Space Invaders on custom hardware because the existing CPUs could not keep up. The TMS9900 could not move enough sprites fast enough. So he designed the chips himself.

There is an accident in Space Invaders that became a feature: as the player shoots the aliens, there are fewer of them to draw. Fewer sprites means the CPU has spare cycles. The game speeds up. The accidental acceleration was playtested, felt right, and kept. The difficulty curve is a CPU utilization chart.

What it is: a game shaped by its own hardware constraints. The machine's limits became the drama.

---

## Hunt the Wumpus (Gregory Yob, 1973)

Written in BASIC. The Wumpus lives in a cave of twenty rooms arranged as a dodecahedron — twelve pentagonal faces, thirty edges, twenty vertices. The player navigates by edge connections without seeing the map. The cave is a graph. The game is topology.

Yob wrote it in protest. The dominant games of the time were grid-based — "find the thing in the 10×10 grid." He wanted a different topology. So he chose one.

Hunt the Wumpus is the first game with a narrative premise and a non-Euclidean space. Both of these things matter. The Wumpus is a character, even if it is never described. The cave is a world, even if it has no pictures.

What it is: the first game that took topology seriously.

---

## Colossal Cave Adventure (Crowther & Woods, 1976)

Will Crowther was a caver and a programmer at BBN — one of the firms that built ARPANET. He mapped Mammoth Cave in Kentucky with his daughters in mind. Then he translated the map into a FORTRAN program and added a dragon and some treasure.

Don Woods found the source code on a ARPANET server in 1976, emailed Crowther for permission, and expanded it. The result is *Adventure*: the first text adventure, and the template for everything that followed.

"You are standing at the end of a road before a small brick building. Around you is a forest. A small stream flows out of the building and down a gully."

This is writing. The machine is the author; the player is the reader who also acts. The map is a narrative. Every room description is a sentence. The game is a novel you play with your body.

What it is: the first proof that a computer could be a storytelling machine.

---

## Zork (MIT, 1977 / Infocom, 1980)

A group at MIT — Blank, Daniels, Lebling, Moriarty — built Zork on a PDP-10, then commercialized it through Infocom. The parser understood natural language: not just GO NORTH and TAKE LAMP but PICK UP THE BRASS LANTERN and PUT IT IN THE TROPHY CASE. The machine was reading you.

Infocom became the great literary game studio. *Hitchhiker's Guide to the Galaxy* (with Douglas Adams), *A Mind Forever Voyaging*, *Trinity* — games with genuine literary ambition, written by people who had read things.

The Zork source code is online. Reading it is reading a natural language parser built in MDL (a Lisp dialect), in 1977, by people who wanted to make the computer a reader.

What it is: the computer as interlocutor. Writing that writes back.

---

## Pac-Man (Namco, 1980)

Toru Iwatani. The design brief was to make a game women would play — the arcade was a male space. Iwatani thought about eating, about a pizza with a slice missing. The maze is a graph. The ghosts have personalities — Blinky chases directly, Pinky targets ahead of Pac-Man, Inky is erratic, Clyde runs away when too close. Four distinct algorithms for four distinct characters.

Pac-Man introduced the idea that non-player characters could have *behavior*, not just movement. The ghosts are the first NPCs. Their code is their personality.

What it is: character as algorithm.

---

## Donkey Kong (Nintendo, 1981)

Miyamoto's first game. He had been asked to turn an unsold Radar Scope cabinet into something new. He designed a three-level platformer with a narrative: the ape takes the girl, the carpenter climbs to save her. The carpenter was called Jumpman. He later became Mario.

Miyamoto thought in spatial metaphors. "Donkey Kong" is a mistranslation — Miyamoto intended "stubborn ape" but his English was limited. The name stuck.

What it is: the first platformer with a narrative arc, however simple.

---

## Super Mario Bros (Nintendo, 1985)

The tutorial without a tutorial. World 1-1 teaches the controls without text. The first Goomba approaches from the right. Either you jump or you don't. If you don't, you die, and you learn what the Goomba is.

This is writing. The level is the text. The player's body is the reader. The designer is the author who built a reading experience that works without words.

Miyamoto designed levels by drawing on graph paper, room by room, then playing them. He revised them the way a writer revises paragraphs. The finished game is the manuscript.

What it is: spatial prose. Reading with your thumbs.

---

## The Legend of Zelda (Nintendo, 1986)

An open world before "open world" existed. Miyamoto wanted to give players a miniature garden to explore. The map is the narrative. The dungeon keys are the chapters. The overworld is the space between.

Link's inventory is a writing system: each item a symbol, each combination a sentence. The boomerang plus the candle plus the bombs is a grammar for navigating space.

The original Zelda source has not been released. But it has been reverse-engineered and documented. Reading the disassembly is reading the argument Miyamoto was making, recovered from the machine.

What it is: the map as novel. Exploration as reading.

---

## Tetris (Alexey Pajitnov, 1984)

Moscow. The Soviet Academy of Sciences. Pajitnov was a researcher; Tetris was a thought experiment that got out of hand.

The game has no story. No characters. No level design in the Miyamoto sense. It is a pure puzzle — shapes falling, the player imposing order on entropy. And it is one of the most played games in human history.

The Tetris legal battles — who owned the rights, in what country, under Soviet law — are a complete story about what it means to own a piece of writing, and what it means to not be able to own it.

What it is: the puzzle without a narrative. Order against time.

---

## Doom (id Software, 1993)

Released as shareware on December 10, 1993. The first episode free. The source code later released under the GPL.

Doom is the direct predecessor of Quake and shares most of the same characters. Where Quake has BSP trees, Doom has a simpler sector-based engine. Where Quake is true 3D, Doom is 2.5D — the floors and ceilings exist, but you cannot aim up or down.

The WAD file format — Where's All the Data — is one of the great data-driven designs in game history. The engine is separate from the content. The levels, textures, and enemies live in WAD files. This made Doom moddable from birth. The community built thousands of WADs. Some are still being made.

What it is: the engine and the content separated. The first great modding platform.

---

## Minecraft (Mojang / Markus Persson, 2011)

Notch built the first version in a weekend. The procedural generation means every world is unique. The creative mode means the player is the designer. The redstone system is a complete logic circuit simulator — players have built working computers inside Minecraft.

Minecraft is the closest a game has come to collapsing the distinction between player and author. In creative mode, the player writes the world. The redstone computer is a program running inside a program.

And yet: the player cannot see the code. The box is still closed. The final level is still on the other side of the screen.

What it is: the sandbox that almost opened the door.

---

## The Argument This Garden Makes

Pong (1972) → Adventure (1976) → Zork (1977) → Mario (1985) → Zelda (1986) → Doom (1993) → Quake (1996) → Minecraft (2011)

This is a history of writing technologies wearing the costume of entertainment. Each game is a different argument about what reading and writing can be — what it feels like to be a reader, how much agency the reader has, what happens when the reader can respond.

The games get richer, more open, more participatory. The player gets more authorship. And then, always, a wall: the wall of the closed system. You can place blocks but not write code. You can build levels but not design engines.

Coding removes the wall.

The person who learns to read source code — who can open Quake's renderer and understand what it is saying — is not just a more powerful player. They are a different kind of person. A person who can write to machines, not just receive from them. A person with the full access that games always promised and never quite delivered.

The final level of any video game is coding. We are already there.
