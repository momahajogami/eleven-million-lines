# Unit 06: Languages and Theory

*Before C, there was assembly. Before assembly, there were punch cards. Before punch cards, there was a loom.*

---

## The thread

In 1801, Joseph Marie Jacquard demonstrated a loom controlled by punched cards. Each card encoded the pattern for one row of weaving: a hole meant the warp thread lifted, no hole meant it stayed down. Binary. Programmable. The pattern was not woven into the loom — it was stored separately, on cards, and read by the machine during operation. The program and the machine were distinct.

Ada Lovelace understood this. When she wrote her notes on Charles Babbage's Analytical Engine in 1843 — the notes that contain what is widely considered the first computer program — she described the Engine as capable of weaving algebraical patterns just as the Jacquard loom wove flowers and leaves. She was not being poetic. She was being precise. The punch card mechanism that Babbage proposed for the Engine was directly inherited from the Jacquard loom. The metaphor was an accurate description of the architecture.

The line runs from the Jacquard loom (1801) to Babbage's designs (1830s–1870s) to Hollerith's census tabulation machine (1890, punch cards for data) to the IBM card (1928) to the first stored-program computers (1940s) to the languages that told those computers what to do.

This unit follows that line and then branches.

---

## What a programming language is

A programming language is a notation for expressing computation — a writing system for programs. Like all writing systems, it embeds assumptions about what needs to be said and what can be left unsaid. Like all writing systems, it has a history, a community of practice, and debates about correctness and style that outlast any individual practitioner.

The history of programming languages is the history of a series of answers to the question: *what should the machine be hiding?*

Assembly language hides nothing. The programmer specifies every instruction the processor executes. The notation is almost one-to-one with the machine's instruction set. The abstraction is minimal: instead of binary opcodes, you write mnemonics (MOV, ADD, JMP). The machine does exactly what you say.

FORTRAN (1957) hid the register allocation. You wrote arithmetic expressions; the compiler figured out which registers to use. This was considered almost magical at the time — the idea that a program could write machine code was not obviously possible.

LISP (1958) hid the memory management. McCarthy's garbage collector freed the programmer from tracking every allocation and deallocation. It also embedded a theory: the lambda calculus that Alonzo Church had developed in 1936 as a mathematical foundation for computation. LISP was not just a language — it was lambda calculus made executable.

Each generation of languages answers the question differently, hides something different, embeds a different theory of what computation is. The theories were not invented to serve the languages; many of them preceded the languages by decades. Church's lambda calculus was a mathematical formalism from 1936 that became a programming language in 1958. Turing's computational model, also from 1936, became the conceptual foundation for imperative programming. The theory precedes the practice. The practice makes the theory tangible.

---

## Babbage and Lovelace

Charles Babbage designed the Difference Engine (1822–1842) to compute and print mathematical tables without human error — the tables were full of mistakes made by the human "computers" who calculated them by hand. The Difference Engine was a machine for computing polynomial functions by the method of finite differences. It was never completed in his lifetime.

The Analytical Engine (designed from 1837) was something different and greater: a general-purpose mechanical computer with a mill (processor), a store (memory), an input mechanism (punch cards), and a printer. It was Turing-complete, though the concept of Turing completeness would not be formulated for another hundred years. Babbage built partial prototypes. The full machine was never built in his lifetime.

Ada Augusta King, Countess of Lovelace — daughter of Lord Byron, mathematician, collaborator — met Babbage in 1833. In 1843 she translated an article about the Analytical Engine written by the Italian mathematician Luigi Menabrea, and added notes that were substantially longer than the original article. Note G contains an algorithm for computing Bernoulli numbers — a sequence of computations to be performed by the Engine, step by step, with a loop and a conditional. It is the first computer program in the sense that matters: a complete, correct description of a computation intended for execution by a machine.

Read it in `06/scratch/lovelace-notes.txt`. Read it slowly. It is 1843. The machine the program is intended for does not yet exist. The person writing it understands, more clearly than anyone else at the time, what the machine could be: not a calculator, but a general engine of computation. Her phrase — "the Engine might compose elaborate and scientific pieces of music of any degree of complexity or extent" — predates the MP3 by 150 years. She was right. She knew she was right. The machine just wasn't built yet.

---

## Church and Turing

In 1936, two people on different continents, working independently, solved the same problem.

The problem was David Hilbert's *Entscheidungsproblem* — the decision problem: is there a mechanical procedure that can determine, for any mathematical statement, whether it is provable? If yes, mathematics could in principle be automated. Every theorem would be decidable by an algorithm.

Alonzo Church answered no, using lambda calculus — a formal system for defining and applying functions. His paper, "An Unsolvable Problem of Elementary Number Theory" (1936), proved that there are well-defined mathematical problems that no algorithm can solve.

Alan Turing answered no, using a different formalism — a hypothetical machine that reads and writes symbols on a tape according to rules. His paper, "On Computable Numbers, with an Application to the Entscheidungsproblem" (1936), proved the same result with a different tool, and along the way defined the concept of computation itself.

These two formalisms are equivalent. Church's lambda calculus and Turing's machine model compute exactly the same class of functions. This equivalence — the Church-Turing thesis — is the foundational claim of theoretical computer science: any effective computation can be carried out by a Turing machine, and any Turing machine can be simulated by lambda calculus, and any lambda calculus expression can be computed by a Turing machine.

Lambda calculus became LISP. Turing machines became the conceptual model for every procedural programming language. The theoretical tools from 1936 are the foundations of the languages you use today.

Both papers are in `06/scratch/`. Read them. They are not easy. They are worth the difficulty.

---

## The languages

### Assembly — *The machine's mother tongue*

Assembly language is the thinnest possible layer between the programmer and the processor. Each instruction in assembly corresponds (almost) directly to one instruction the CPU executes. MOV copies data. ADD adds. JMP jumps. CMP compares. The programmer manages registers, addresses, and flags explicitly.

This is tedious. It is also clarifying. When you have written non-trivial assembly, you understand what a high-level language is hiding — and hiding well. You understand what a C compiler is doing when it compiles an if-statement. You understand why buffer overflows happen at the memory level. You understand why the stack grows downward on x86.

The connection to textiles: the Jacquard loom's punch cards were a kind of assembly language — each card specified one row of operations, directly and mechanically. There was no abstraction above the cards. The program and the execution were essentially the same thing.

The connection to punch cards: early stored-program computers were programmed by toggle switches, then by paper tape, then by punch cards. The IBM 80-column card was the programming medium for a generation of programmers who could not interact with their programs in real time. You submitted a deck and waited for output. Error on card 47. Resubmit.

**What to look at:** `06/nasm/` — the Netwide Assembler. Read a small assembly program. `06/scratch/hello-world.asm` is the canonical example. Understand what the linker does with it.

### BASIC — *The democracy of computing*

John Kemeny and Thomas Kurtz created BASIC at Dartmouth in 1964 to give students with no programming background access to computing. The goal was explicit: a language so simple that a liberal arts student could learn it in an afternoon, running on a time-sharing system so that many students could use the computer simultaneously.

BASIC was not sophisticated. It was interpreted (slow), line-numbered (awkward), and lacking in abstraction (GOTO everywhere). But it ran. And when the microcomputer arrived in the mid-1970s, BASIC was there — small enough to fit in the ROMs of machines with 4KB of memory, simple enough to be learned from the manual. The Altair 8800 (1975) shipped with a BASIC interpreter written by two young programmers: Bill Gates and Paul Allen. Apple I, TRS-80, Commodore 64 — all shipped with BASIC in ROM.

A generation of programmers learned to program in BASIC. Not because it was the best language but because it was the language that was *there*, on the machine, waiting, when they turned it on. This is not nothing. The first language you learn marks you. The BASIC generation grew up thinking procedurally, with line numbers and GOTOs, before they learned that other things were possible.

The BASIC story is a story about access. Kemeny and Kurtz were thinking about Dartmouth students. They could not have imagined the Commodore 64. The language outlived its context by two decades because it was simple enough to fit anywhere and good enough to get started.

**What to look at:** `06/scratch/hello-basic.bas` — a small BASIC program. Compare it to `06/scratch/hello-world.asm`. They do the same thing. Look at the distance between them.

### LISP — *Lambda made executable*

John McCarthy invented LISP at MIT in 1958. He was trying to implement his ideas about symbolic computation — programs that manipulate other programs, lists that represent both code and data — and he needed a language that could express these ideas.

The result is the oldest high-level language still in widespread use, and the one with the most direct connection to mathematical theory. LISP is lambda calculus with parentheses and a runtime. The two fundamental operations — car (first element of a list) and cdr (rest of a list) — are sufficient to construct any data structure. The homoiconicity — code and data have the same representation — means that a LISP program can generate and execute other LISP programs at runtime. Macros in LISP are programs that write programs.

McCarthy's 1960 paper "Recursive Functions of Symbolic Expressions and Their Computation by Machine" contains a complete implementation of a LISP interpreter in LISP itself — a metacircular evaluator, LISP defined in LISP. This is one of the most beautiful pieces of computer science writing in existence. It is in `06/scratch/`.

Emacs Lisp, which you read in Unit 03, is a descendant. Common Lisp. Scheme. Clojure. The family is large and still alive. Every language with macros — Rust, Julia, Elixir, most of the interesting ones — owes something to what McCarthy figured out in 1958.

**What to look at:** `06/scratch/mccarthy-1960.txt` — the paper. Read Section 3, which contains the metacircular evaluator. Then run the Scheme examples in `06/scratch/`.

### ML and Haskell — *Type theory and purity*

In the 1970s, Robin Milner at Edinburgh developed ML — a language for theorem proving that introduced type inference (the compiler figures out the types; you don't have to declare them) and algebraic data types (types that are defined by their cases, like a mathematical inductive definition). ML is the ancestor of OCaml, F#, Scala's type system, Rust's type system, and much of what modern statically-typed languages consider obvious.

Haskell (1990) pushed further: a purely functional language, lazy by default (expressions are only evaluated when needed), with a type system expressive enough to encode complex invariants about program behavior. Writing Haskell forces you to think about what your program is computing rather than how it computes it.

These languages are not practical in the same way that C or Python is practical. They are important because they pushed the frontier of what type systems can express, and those ideas have propagated into languages that are practical. Every time a Rust compiler catches a memory bug at compile time, it is using ideas that ML and Haskell developed.

**What to look at:** `06/ghc/` — the Glasgow Haskell Compiler. The GHC source is itself written largely in Haskell. This is the metacircular dynamic at work again: a language sophisticated enough to implement its own compiler. Read the type checker (`compiler/GHC/Tc/`).

### Prolog — *Logic as computation*

Prolog (1972, Alain Colmerauer) is a language in which you state facts and rules, and the runtime finds solutions. You do not tell the computer how to solve the problem. You describe the problem, and the computer searches for answers.

This is a fundamentally different model of computation — logic programming instead of procedural programming. Prolog is Turing-complete (it can compute anything a Turing machine can), but the way you express computation is to define what is true rather than what to do.

Prolog was briefly extremely prominent in the 1980s — Japan's Fifth Generation Computer Systems project was built on it. It fell from prominence not because it failed but because the problems it was best suited for (natural language parsing, symbolic AI) turned out to be harder than expected, and the procedural and functional approaches got better faster.

It belongs in this unit because it represents the logical branch of the computational family tree — the branch that descends from formal logic and theorem proving rather than from the Turing machine model. The two branches are equivalent in power but radically different in how you think while using them.

---

## The papers

All foundational papers are in `06/scratch/`:

- `lovelace-notes.txt` — Ada Lovelace's notes on the Analytical Engine, 1843 (Note G contains the first program)
- `turing-1936.txt` — "On Computable Numbers, with an Application to the Entscheidungsproblem"
- `turing-1950.txt` — "Computing Machinery and Intelligence" (the Turing test paper)
- `church-1936.txt` — "An Unsolvable Problem of Elementary Number Theory"
- `mccarthy-1960.txt` — "Recursive Functions of Symbolic Expressions and Their Computation by Machine"

Read them in this order. Each one is a response to the questions the previous ones raised.

---

## The textile thread, completed

The Jacquard loom stores pattern as hole/no-hole. The Hollerith machine reads data as hole/no-hole on a paper card. The stored-program computer reads instructions as 0/1 in memory. The assembly programmer writes those 0s and 1s as mnemonics. FORTRAN abstracts the mnemonics into arithmetic expressions. LISP abstracts further, into symbolic computation. ML adds types. Haskell adds purity. Prolog adds logic.

Each step adds abstraction. Each step hides something. The thing hidden is not lost — it is still there, at the bottom. Assembly sits below C. Machine code sits below assembly. 0s and 1s sit below machine code. Holes and no-holes sit below 0s and 1s.

Lovelace knew this. She was working at the bottom, where the abstraction hadn't started yet, and she described what was there with perfect clarity. The Analytical Engine would weave algebraical patterns just as the Jacquard loom wove flowers and leaves. She was right. She was two hundred years ahead of us and she was right.

---

## What to do

1. Read the Lovelace notes. Find Note G. Read the Bernoulli number algorithm. Understand what it is doing step by step. It is a loop with a conditional — the same structure as any for loop in any language.

2. Read the Turing paper (1936) sections 1–3. Understand what a Turing machine is. Then understand what the halting problem is. These are the same idea: some questions about programs cannot be answered by programs.

3. Write "Hello, World" in assembly (see `06/scratch/hello-world.asm`), compile and run it. Then write it in a high-level language of your choice. Measure the distance.

4. Read McCarthy's metacircular evaluator. Implement it, or the core of it, in a language you know. You are implementing a programming language. The experience is different from using one.

5. Open the GHC source in `06/ghc/`. Find the type checker. Read the file header. You are looking at one of the most sophisticated type systems in existence, implemented in the language it type-checks.

---

*Open* `06/scratch/lovelace-notes.txt` *first. The thread starts there.*
