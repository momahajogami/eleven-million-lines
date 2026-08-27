# Lichess

*A problem to solve. They smashed it.*

---

## Thibault

In 2010, a French programmer named Thibault Duplessis — username ornicar on GitHub — built a chess website as a hobby project. He was not trying to compete with Chess.com or the Internet Chess Club. He was trying to make something he wanted to exist: a fast, clean, free chess server with no ads, no subscriptions, no premium tiers, no limitations.

He called it Lichess.

The first versions were rough — PHP on a shared server, minimal features, small audience. But the idea was precise and right: every feature free. No registration required to play. The games are yours — download them. The code is yours — it's all open source.

Thibault rewrote Lichess in Scala — a statically typed functional language running on the JVM — with the Play Framework. The rewrite, called **lila** (Li-chess in scAla), gave the server the architecture it needed to scale. Scala's type system catches an entire class of bugs before the program runs. Akka's actor model handles thousands of simultaneous game state updates without the coordination overhead that would crush a simpler threading model.

For the layer between the internet and the application — the Nginx web server handling HTTP, WebSockets, and connection routing — Lichess used Lua via OpenResty. OpenResty embeds LuaJIT directly into Nginx, allowing application logic to run at the web server level itself. Game state broadcasts, connection routing, move delivery at the edge: Lua scripts, running in the fastest layer of the stack, handling what the application server should not have to see.

This is engineering elegance: place logic where the cost is lowest. Use a language built for embedding in systems where speed is the constraint. Lua is small, fast, and designed to disappear into the surrounding architecture. You saw it in Blender (Unit 04). You will see it in game modding, in embedded firmware, in network infrastructure. It is the language of the interstice — lightweight, purposeful, designed to live inside something bigger.

---

## The integration

As Lichess grew, it integrated Stockfish.

Every game played on Lichess can be analyzed, after the game ends, by Stockfish running on Lichess's servers. The engine finds the mistakes, shows the better moves, gives each position a numerical evaluation and a line. This is what chess teachers do — and Lichess does it for free, for everyone, after every game.

Later, Lichess compiled Stockfish to WebAssembly and ran it in the browser itself. The strongest chess engine in the world, executing in a browser tab, analyzing positions on your hardware, requiring no account, no installation, no cost.

The contrast with 1997 is complete. Deep Blue: a $10 million corporate machine, retired after the match, inaccessible to everyone. Stockfish on Lichess: open source, free, running on your phone, analyzing your club game in the browser.

---

## What it changed

Before Lichess, serious chess study required:
- An engine license ($50–$100 for Fritz, Hiarcs, Rybka)
- A database subscription (ChessBase — hundreds of dollars)
- Access to strong players for analysis
- Resources that most people in most places did not have

Lichess removed all of these. The engine runs in the browser. The game database holds hundreds of millions of games. The puzzles — millions of them, generated automatically from real games, graded by difficulty — are free. The studies — annotated game collections — are public and shareable.

This is what it looks like when a problem is actually solved. Not mitigated, not improved, not made slightly more affordable. Solved. The barrier that once separated serious chess study from casual chess play no longer exists. A student in rural Ohio and a student in rural Nigeria and a student in a Moscow apartment have the same access to the strongest analysis tool ever built.

---

## The social magic of chess

There is something unusual about Lichess as a social space.

You play a stranger. You do not know their name. You cannot see them. The entire interaction is the movement of pieces on a board. When the game ends, there is a chat window.

And almost always — with remarkable regularity, given that this is the internet — the exchange is respectful. "Good game." "Thanks." Sometimes: "Nice endgame." Sometimes a longer conversation about the position, the line you both missed, the move neither of you saw until after.

This is not the normal experience of interacting with strangers online. Social media is polarized. Comments sections are hostile. Forums are territorial. But chess, somehow, consistently produces courtesy.

The reason may be structural. Chess demands your full attention. While you are playing, you are not thinking about the other person as someone to evaluate or argue with — you are thinking about the position. They are also thinking about the position. The position is the thing you share. When the game ends, you have been through something together. You tested each other. The pieces were your proxies and they performed well or poorly, and now the game is over, and you were both present for it.

*In literature, chess is often used to show intimacy.* It appears in Nabokov, in Zweig, in Carroll, in Calvino. It appears when two people need to be in the same room, focused together on a shared problem, without having to say what they are actually to each other. The board is the excuse, and the cover, and eventually the truth.

The pieces have a quality that playing cards and coins do not: they are characters. The king who cannot be fast but cannot be lost. The queen who moves everywhere and must never be risked carelessly. The bishop who cannot leave its color — a creature permanently committed to one diagonal of the world. The pawn who can become something else if it survives long enough. These figures awaken something — they are wood, they are abstract, and yet they feel alive the way a well-turned sentence feels alive: as though someone made choices that carry weight.

We respect each other when we play chess. Not because chess players are unusually good people, but because the game creates conditions for respect. You are trying to make something good — a position, a plan, a combination — and then you are deliberately offering it to your opponent to attack. You *want* them to try to break it. If it breaks, you learn where it was weak. If it holds, you learn where it was strong.

The opponent is not your enemy. The opponent is the test.

---

## Testing code

This is the same thing as testing code.

Stockfish's testing methodology — Fishtest, the SPRT, the patch-versus-baseline framework — is a chess game between two versions of the same program. The patch sits across the board from the current version. They play. The result is honest.

The contributors who submit patches are not competing against each other. They are competing against themselves — against the previous version of themselves that wrote the last patch. Each submission is a question: *is this better?* The answer comes from the game.

Your good friends are not the ones who flatter you. The ones who tell you the position is fine when it isn't — they are not helping you. They are making you comfortable while the clock runs.

The game board is honest. The test suite is honest. The patch that loses its games teaches you more than the patch that wins your approval.

We are not, when we submit code to review, competing against our reviewers. We are competing only against ourselves — against who we were when we wrote the previous version. The reviewer is the opponent. And the opponent is what makes the game real.

---

## The project

Lichess is a great example of what a project can be.

There was a problem: chess analysis and online play required money, which meant access was unequal, which meant the game's reach was artificially limited. Thibault saw this clearly and decided to solve it. He built the thing. He made it free. He made it open source. He kept the servers running on donations. He found collaborators who shared the commitment.

The result is a server that now hosts millions of games per day, that has given millions of people access to serious chess study for the first time, that runs the strongest analysis engine ever built in a browser tab for free.

It is not a company with a growth strategy. It is a solution to a problem, built by someone who wanted the solution to exist.

The code is at `09/other-games/lichess/`. It is large. Start with the README and the module structure in `modules/`. The Scala is idiomatic and well-organized. The Lua in the Nginx configuration is worth reading — a different language solving a specific performance problem at the right layer of the stack.

Read the code. Then play a game on Lichess. Then analyze it with the free engine. The thing you are analyzing your game with and the thing you are reading in the source directory are the same thing. The code is the tool. The tool is the code.

*This is the final level.*
