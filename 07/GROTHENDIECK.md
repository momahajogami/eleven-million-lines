# Unit 07: The Spiritual

*Alexander Grothendieck. William Lawvere. The mathematics that underlies the mathematics.*

---

## A different kind of unit

Every previous unit has had a codebase at its center — something you can clone and compile and run. This unit has that too (Lean, Agda, Coq, simplicial sets as code), but the center is different. The center is mathematics of a kind that most mathematicians find difficult and most programmers have never encountered, written by two people who thought about structure with an intensity that is almost impossible to describe without sounding like you are exaggerating.

You are not required to master this. No one masters Grothendieck's algebraic geometry in a course, or a semester, or a decade. What this unit offers is something different: a serious amateur's approach. Sustained attention. Willingness to sit with difficulty. The goal is not to understand everything but to understand something — and to feel, at least once, the texture of mathematics at this level.

The word "spiritual" is not casual. Grothendieck himself used it. He described mathematics as a kind of meditation, a contemplation of things that exist before the mathematician arrives and will exist after they leave. He described understanding as something that happens to you when you stop forcing it. He was, by the end of his life, a mystic as much as a mathematician. This unit does not ignore that. It is part of the picture.

---

## Grothendieck

Alexander Grothendieck (1928–2014) was the child of anarchist parents — his father, Alexander "Sascha" Schapiro, participated in the Russian Revolution and the Spanish Civil War; his mother, Johanna "Hanka" Grothendieck, was a writer. He spent part of his childhood in a French internment camp. He studied mathematics under Jean Dieudonné and Henri Cartan. He spent fifteen years at the Institut des Hautes Études Scientifiques (IHÉS) near Paris, where, between approximately 1958 and 1970, he produced a body of work that transformed mathematics.

The transformation was methodological as much as substantive. Grothendieck's approach was to find the most general setting in which a concept made sense, prove the result there, and then derive the specific cases as corollaries. This sounds like a technique. It was a philosophy. He believed that mathematics resisted you when you pushed it in the wrong direction, and yielded naturally when you found the right level of generality. His word for this was *topos* — a word he invented to describe a kind of mathematical object general enough to encompass sets, spaces, logical structures, and more exotic things simultaneously.

The key concepts:
- **Schemes** — a generalization of algebraic varieties that made algebraic geometry vastly more powerful and precise
- **Toposes** — categories that behave like categories of sets but are not; the framework for categorical logic
- **Motives** — a still-conjectural framework for understanding cohomology theories across different mathematical settings; Grothendieck sketched the idea and died before it was complete
- **Descent theory** — how to assemble global objects from local data; how you know that something glued together correctly is actually the thing you wanted
- **The yoga of six operations** — a framework for understanding cohomological operations that unifies many constructions across algebraic geometry

He withdrew from professional mathematics in 1970, after learning that IHÉS accepted military funding. He spent subsequent decades on ecology, pacifism, and eventually a profound isolation in the Pyrenees, where he died in 2014.

His later mathematical writing — *Récoltes et Semailles* (Harvests and Sowings, a 1000-page reflection on his life and mathematics), *La Longue Marche à Travers la Théorie de Galois* (The Long March Through Galois Theory), *Pursuing Stacks* (a letter to Daniel Quillen about homotopy theory that grew into a 600-page vision), and *Esquisse d'un Programme* (Sketch of a Programme) — is unlike anything else in mathematics. It is personal, visionary, and occasionally angry. *Pursuing Stacks* is addressed to a colleague and reads like a very long, very mathematical letter. Read it as a document, not as a textbook.

---

## Lawvere

F. William Lawvere (1937–2023) studied under Sammy Eilenberg — one of the inventors of category theory — and spent his career at SUNY Buffalo. His contributions are less famous than Grothendieck's but equally foundational to the uses of category theory that matter for this course.

His 1963 PhD thesis, "Functorial Semantics of Algebraic Theories," established the categorical foundations of algebra. His 1969 paper "Adjointness in Foundations" argued that adjoint functors — a central concept in category theory — are the fundamental conceptual tool of mathematics, appearing everywhere from logic to physics to computation.

His work with Myles Tierney in the late 1960s and early 1970s established elementary topos theory — a version of Grothendieck's toposes formulated without set theory as a foundation, using only categorical axioms. This is the result Lawvere most wanted: that mathematics could be founded on category theory directly, without needing to go through set theory first.

His connection to computation is direct and important:

**The Curry-Howard-Lambek correspondence** is a three-way equivalence between:
- Intuitionistic logic (a logic without the law of excluded middle)
- The simply-typed lambda calculus (the basis of functional programming type systems)
- Cartesian closed categories (the categorical structure Lawvere and Eilenberg studied)

What this says: a type system and a logic are the same object, described in different language. A proof is a program. A program is a proof. The type checker is a proof verifier. This is the correspondence that underlies Coq, Agda, Lean, and every other proof assistant — and it is Lawvere's categorical framework that makes it precise.

---

## The tools

The tools in this unit are proof assistants — programs in which mathematics is written in a formal language, and the program verifies that the mathematics is correct. They are both programming languages and mathematical notation systems.

### Lean 4 and Mathlib

Lean is a proof assistant developed at Microsoft Research by Leonardo de Moura. Lean 4 (2021) is a complete redesign that is simultaneously a dependently-typed programming language and a proof assistant. **Mathlib** is the community library of formalized mathematics for Lean — currently the largest single repository of formalized mathematics in existence.

The scope of Mathlib is remarkable: it includes real analysis, complex analysis, algebraic geometry (parts of it), number theory, topology, category theory, and much more. When a new theorem is formalized in Lean and added to Mathlib, it has been verified by a computer from first principles. The proofs do not just seem correct; they are machine-verified.

Grothendieck's influence is present in Mathlib's category theory library. Lawvere's adjoint functors are there. Schemes are being formalized. The road from the Jacquard loom to the machine-verified Grothendieck-Riemann-Roch theorem is long, but it is one road.

`07/lean-mathlib/` — the Mathlib repository (large; blobless clone).

### Agda

Agda is a dependently-typed programming language and proof assistant developed by Ulf Norell. Its type theory is a direct implementation of Martin-Löf type theory — the constructive type theory that formalizes the Curry-Howard correspondence.

Agda has been used to formalize homotopy type theory (HoTT) — a connection between type theory and homotopy theory (a branch of algebraic topology that Grothendieck influenced deeply through his concept of higher stacks). The HoTT book (2013) was written collaboratively using Agda, among other tools, and is freely available.

`07/agda/` — the Agda compiler source.

### Simplicial sets

Simplicial sets are combinatorial structures used to study topological spaces in algebraic topology. They are also a foundation for ∞-categories (infinity-categories), which are Grothendieck's homotopy hypothesis made precise: the claim that homotopy types and ∞-groupoids are the same thing.

This is abstract enough that it requires its own introduction. See `07/scratch/simplicial-sets-intro.md`.

---

## How to approach this unit

**Start with Lawvere.** His "Taking Categories Seriously" (1986, TAC reprint) is the best entry point — a short paper arguing that category theory is not a language for describing mathematics but the foundation of mathematics. It is readable, even if the details are difficult.

**Then read Grothendieck's *Esquisse d'un Programme*.** It is a 1984 proposal he submitted for a position (which he did not get). It is a short document — 50 pages — that outlines a vision for mathematics that mathematicians are still trying to understand forty years later. Read it as literature. You will understand parts of it. The parts you do not understand, let rest.

**Then open Lean.** Install it. Open a Mathlib file. Look at a formalized proof of something you know — perhaps the intermediate value theorem, or the fundamental theorem of algebra. You will not understand all of it. Read the parts you can. Notice that each step of the proof is explicit, checkable, machine-verified. This is what Lovelace's algorithm running on the Analytical Engine would have looked like if the Engine had been built.

**Then read *Pursuing Stacks*, the opening.** The first twenty pages are a letter. They are accessible. They are Grothendieck in 1983, telling a colleague what he is thinking about and why. Read it as a letter.

The goal is not understanding in the usual sense. The goal is contact — with a way of thinking about mathematics that is genuinely different from what you have encountered before, and that is connected, through category theory and type theory and proof assistants, to the code you have been reading in every other unit of this course.

---

## What is in 07/

- `lean-mathlib/` — Mathlib, the Lean 4 mathematics library
- `agda/` — the Agda proof assistant source
- `scratch/` — foundational papers and reading guides:
  - `lawvere-taking-categories-seriously.pdf`
  - `lawvere-adjointness-in-foundations.pdf`
  - `grothendieck-esquisse.pdf`
  - `pursuing-stacks-excerpt.pdf`
  - `simplicial-sets-intro.md`
  - `hott-chapter1.pdf` (first chapter of the HoTT book, freely available)

---

## The connection to the rest of the course

Every unit in this course has been about reading — about standing inside large, old, important code and finding your bearings. This unit asks you to do the same with mathematics.

The languages in Unit 06 (Haskell, Agda, Lean) are the executable form of the mathematics in this unit. The Curry-Howard-Lambek correspondence means that a type system and a proof system are the same thing described differently. When you write a Haskell function, you are writing a proof. When you read a Lean proof, you are reading a program. The boundary is not where most people think it is.

Grothendieck's topos theory is, among other things, a foundation for the semantics of programming languages — a mathematical setting in which the meaning of a program can be defined precisely. Lawvere's categorical logic is the framework within which the type theory of Agda and Lean is formulated. The mathematics and the code are not two subjects. They are one subject described at different levels of abstraction.

The Jacquard loom encoded patterns as holes in cards. Babbage designed a machine to execute mathematical notation. Lovelace wrote the first program. Church and Turing formalized computation. McCarthy made lambda calculus runnable. Milner added types. Lawvere showed that types and proofs are the same. Voevodsky (building on Grothendieck's homotopy hypothesis) showed that proofs and homotopies are the same. Lean verifies all of this, mechanically, from axioms.

The thread from the loom runs here.

---

*Start with Lawvere. Then Grothendieck. Then open Lean and find something you know and look at how it was proved. The rest will follow, slowly.*
