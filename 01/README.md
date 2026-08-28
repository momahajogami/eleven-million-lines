# Unit 01 — Early Unix

Three repositories. One tradition. The place where most of what you use was invented.

---

## What is here

**`xv6/`** — A reimplementation of Unix Version 6, written at MIT to be read. Not a museum piece: a teaching instrument, deliberately small, deliberately clear. 9,400 lines. You can hold the whole thing in your head. That is the point.

**`unix-v6/`** — The actual Research V6 source. The code Lions wrote his Commentary about. Rougher than xv6, older, stranger in places — and therefore more honest. This is what it looked like when it was being made rather than explained.

**`plan9/`** — Bell Labs trying again. Rob Pike and Ken Thompson, twenty years on, asking: what would Unix look like if we knew then what we know now? The answer is eerie and elegant and lost a fight it probably deserved to win. Worth reading for what it chose differently.

---

## Paired text

**John Lions, *A Commentary on the Sixth Edition UNIX Operating System* (1977)**

Lions wrote this to teach his students at the University of New South Wales to read Unix source. AT&T said it was proprietary. For years it circulated as a photocopy — illegal to own, treasured anyway. Code as samizdat. It was finally published legally in 1996.

The Commentary is structured simply: the source code on the left page, Lions's annotations on the right. That structure is the model for everything in `commentary/`.

---

## How to approach these repos

The repos are primary texts. They are not modified, annotated in-place, or treated as raw material. You read them the way you read a book someone else wrote — with attention, with respect for what they chose, with your own notes kept separately.

`commentary/` is where the notes live.

---

## Mood

Bell Labs, 1972. Things were typically well made. People felt at times like they were breaking convention, but the conventions were there like solid ground beneath you. It was a moment carved out to host for a few decades the life of the mind, and great things were accomplished.

The code that came out of that building is inseparable from the world that produced it. Unix is not just a technical achievement — it is an artifact of a particular moment, when people believed you could build things that lasted.

---

## Reading order

Start with `commentary/xv6/entry.md`. Get your bearings. Then open the source.

---

## Further reading

- **Lions' Commentary on UNIX 6th Edition** (John Lions) — the original; xv6 was built to be read alongside it
- **The xv6 book** — MIT's free PDF companion; walks through every subsystem (`pdos.csail.mit.edu`). Also available as a source booklet PDF for Track B students who prefer not to use vim.
- **The C Programming Language** (Kernighan & Ritchie) — written by the people who wrote Unix
- **Operating Systems: Three Easy Pieces** (Arpaci-Dusseau) — free online; excellent on processes, memory, filesystems
- **Unix Internals** (Uresh Vahalia) — for when xv6 feels too simple and you want the real Unix internals
- **PC Assembly Language** (Paul Carter) — free; covers x86 at the right level for reading kernel assembly
