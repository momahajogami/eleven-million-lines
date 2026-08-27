# Stockfish

*The strongest chess engine in the world. Free. Open source. Built by strangers on the internet who love chess.*

---

## The lineage

Stockfish did not appear from nowhere.

Its ancestor is Glaurung — named after a dragon in Tolkien's legendarium — written by Tord Romstad, a Norwegian chess player and programmer, and released in 2004. Romstad wanted a free, strong engine. Not for competitive purposes, not to sell, but because he believed strong chess software should be available to anyone who wanted to study the game.

Glaurung was strong and open source. Marco Costalba, a software developer in Italy, began contributing improvements. In 2008, Costalba collaborated with Romstad and Joona Kiiski — a Finnish programmer who had been working on engine improvements independently — to create Stockfish, combining what each of them had learned. The name is plain and northern: a stockfish is a dried cod, preserved by cold air on Norwegian racks, built to last.

The first versions competed with commercial engines. Within a few years, Stockfish was the strongest engine in the world. Fritz, Hiarcs, Shredder — programs people had paid $60 or $100 for — were weaker than something you could download at no cost.

---

## What Stockfish is

Stockfish is a traditional alpha-beta search engine with sophisticated evaluation. It works by:

1. **Search**: exploring a tree of possible positions, using alpha-beta pruning to cut branches that cannot improve the best known result
2. **Evaluation**: assigning a numerical score to each position based on material count, piece activity, king safety, pawn structure, and dozens of other features
3. **Move ordering**: examining the most promising moves first so that pruning cuts more branches
4. **Time management**: deciding how long to think based on the position's complexity and the time available

The evaluation function was, for years, hand-tuned by contributors — each parameter representing accumulated chess understanding encoded as a number. The question "how much is a bishop pair worth?" is answered in Stockfish's evaluation function with a specific number that was arrived at by years of testing.

Since 2020, Stockfish has incorporated a neural network (NNUE — Efficiently Updatable Neural Network) to evaluate positions. The network is trained on positions evaluated by Stockfish itself. Traditional search, neural network evaluation. The result is significantly stronger than either alone.

The source is C++. It is clean and well-organized — maintainable code written by people who are also chess players, who care that the structure reflects the thinking. Read `src/evaluate.cpp` and `src/search.cpp` for the core logic.

---

## Fishtest and the art of the patch

The central engineering problem of a chess engine is measurement: how do you know if a change makes the engine better?

The answer sounds simple: play games. A stronger engine wins more games against a weaker one. But chess is noisy — a stronger player can lose to a weaker one by blunder. To confidently distinguish a real improvement from statistical fluctuation, you need thousands of games.

Playing thousands of games on your own computer is slow. Playing them on thousands of computers simultaneously is fast.

**Fishtest** is the distributed testing framework built for this. Contributors run a client that downloads two builds of Stockfish — the current baseline and the candidate patch — and plays them against each other in the background while they do other things. The results report back to a central server. The **Sequential Probability Ratio Test (SPRT)** determines when enough games have been played to make a confident decision: this patch is better, or this patch is not.

SPRT is elegant. It does not require you to specify in advance how many games you need. It stops as soon as the evidence is strong enough — either for acceptance or rejection — which is almost always faster than a fixed-sample test. A clear improvement is confirmed quickly. A marginal one takes longer. A neutral or harmful patch is rejected and the contributor learns where to look next.

The result is a meritocracy with a clear, objective criterion. You cannot argue that your patch is better. You demonstrate it, in games, against the current version. The community does not award seniority. It awards wins.

---

## The culture of improvement

This created something unusual: fierce, enthusiastic competition to improve a single program.

Contributors submit patches, wait for Fishtest results, have patches rejected after 50,000 games, revise, resubmit. The question — *can I make this engine play better chess?* — turns out to be deeply motivating in a way that most open source contributions are not. Chess has a score. The score does not lie.

A patch that improves Stockfish by a fraction of an Elo point — a difference that no human would notice in a single game — still represents a real improvement that gets accepted. The standard is high because the measurement is precise.

The unimproved version is the opponent you have to beat. Not another contributor. Not a commercial product. The last version of yourself.

This is the testing parallel the course keeps returning to: your good friends are not the ones who tell you the position is fine. They are the ones who find the refutation. The test suite does not flatter you. It tells you the truth, and the truth is useful.

---

## Exploring the code

```bash
git clone https://github.com/official-stockfish/Stockfish
cd Stockfish/src
make -j build ARCH=x86-64-modern
```

Start in `src/`:
- `main.cpp` — the entry point and the UCI protocol loop
- `search.cpp` — the alpha-beta search
- `evaluate.cpp` — the evaluation function
- `position.cpp` — the board representation
- `movegen.cpp` — move generation

Read `search.cpp` slowly. The alpha-beta loop is one of the most important algorithms in computer science, and Stockfish's implementation is among the most refined in existence.

The early history is in the git log. Stockfish has been in continuous development since 2008; the commit history is a record of a community of people who cared enough to contribute a small improvement, test it honestly, and let it stand or fall on the result.

---

## What Stockfish changed

Before Stockfish, studying chess at a deep level required money. After Stockfish, it requires only time.

The average strength of club-level chess has improved measurably since free strong engines became available. Players who had plateaued found their games analyzed, their weaknesses identified. The feedback loop that strong players had always had — play, analyze, understand, improve — became available to everyone.

The grandmaster's preparation, which once required expensive database software and proprietary engines, is now done with Stockfish. The student's homework, which once required a coach to explain the mistake, is now done with Stockfish. The difference in access between a player with resources and a player without them narrowed significantly.

The game did not become easier. The standard rose, because everyone's access to analysis rose together.

Deep Blue defeated Kasparov and retired into a museum. Stockfish defeated Deep Blue, is available for free on your phone, and is still being improved by strangers on the internet who love chess.

The open source model, applied to a domain with an honest measurement — the game result — produced the strongest chess engine ever built, and then gave it away.
