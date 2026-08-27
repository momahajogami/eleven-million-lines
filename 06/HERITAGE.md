# Heritage — Unit 06: Languages and Theory

*Before there were programming languages, there were people who needed to say something that had never been said before.*

---

## Ada Lovelace (1815–1852)

She was seventeen when she met Charles Babbage at a dinner party in London. He showed her drawings of the Difference Engine — a mechanical calculator he had not yet built. She was the daughter of the poet Byron, raised by a mother who insisted on mathematics as a corrective to her father's dangerous romanticism. She understood what she was looking at immediately.

Babbage spent the rest of his life designing machines. In 1840 he lectured in Turin about the Analytical Engine — a more ambitious design, capable in theory of any computation. An Italian mathematician named Luigi Menabrea published notes on the lecture in French. Babbage asked Lovelace to translate them into English.

She translated the notes, then added her own. The notes she added — labeled A through G — are longer than the original. Note G contains what is now recognized as the first algorithm written for a computing machine: a procedure for calculating Bernoulli numbers. She was twenty-seven.

Note G also contains something rarer: she understood what the machine was. Not a calculator, but a manipulator of symbols — any symbols, not just numbers. "The Analytical Engine," she wrote, "has no power of originating anything. It can only do what we order it to perform." This is still the best one-sentence description of what a computer does.

She died of uterine cancer at thirty-six. Babbage lived to eighty. The Analytical Engine was never built.

---

## Alonzo Church (1903–1995)

In 1928, David Hilbert posed the *Entscheidungsproblem* — the Decision Problem: is there a mechanical procedure that can determine, for any mathematical statement, whether it is provable?

In 1936, Alonzo Church answered it: no. His proof used lambda calculus — a formal system for expressing computation through function application and substitution. Church showed that the halting problem for lambda calculus is undecidable: there is no general procedure for determining whether a lambda expression will reduce to a value or run forever.

Lambda calculus is the mathematical object that LISP is made of. Every functional programming language — Haskell, ML, Scheme, Erlang, large parts of Scala and Rust — is descended from Church's 1936 paper. When you write a function and pass it to another function, you are writing lambda calculus. The notation has changed. The logic has not.

Church taught at Princeton for nearly forty years. He was methodical, careful, and not given to drama. His students included Alan Turing, who was working on the same problem from a completely different direction.

---

## Alan Turing (1912–1954)

Six months after Church's paper, Turing published his own answer to the Entscheidungsproblem — independently, using a completely different approach. He imagined a machine: an infinitely long tape divided into squares, a read-write head that could examine one square at a time, a finite set of states, and a table of rules specifying what to do in each state. The machine could compute anything computable. Turing proved that no such machine can determine, in general, whether any given machine will halt.

When they read each other's papers, Church and Turing realized their results were equivalent. What a Turing machine can compute is exactly what lambda calculus can compute. This equivalence — the Church-Turing thesis — is the foundation of all computer science. The thesis says: anything we would intuitively recognize as a computational procedure can be performed by a Turing machine. We have not found a counterexample in ninety years.

Turing was twenty-four when he published the paper. He had never taken a formal logic course.

During the Second World War, he worked at Bletchley Park, where he led the team that broke the German Enigma cipher. The estimates vary, but most historians believe this shortened the war by at least two years and saved millions of lives. He was awarded the Order of the British Empire for his war work — a decoration he received privately, since the work itself remained classified until the 1970s.

After the war, he worked on early computers, wrote papers on machine intelligence and morphogenesis, and was prosecuted in 1952 for "gross indecency" — homosexual acts, then illegal under British law. He was convicted. He accepted chemical castration — a course of oestrogen injections — as an alternative to prison. He lost his security clearance and his access to classified work.

He died on June 7, 1954. He was forty-one. A half-eaten apple was found by his bed; it tested positive for cyanide. The coroner ruled suicide. His mother believed it was an accident. The truth is not known.

In 2013, the British government issued a posthumous royal pardon. In 2021, Turing's face appeared on the fifty-pound note.

---

## John McCarthy (1927–2011)

In 1958, McCarthy invented LISP at MIT. He wanted a language that could express the symbolic manipulation problems of artificial intelligence — not number crunching, but reasoning, inference, the manipulation of structured knowledge. He built it on Church's lambda calculus, made functions first-class objects, and invented garbage collection (automatic memory management) because he didn't want to think about it manually.

LISP was the first language with a REPL — a live read-eval-print loop where you type an expression and immediately receive a value. The programmer and the machine in immediate dialogue. Every modern interactive environment — Python's shell, Node's console, the Haskell interpreter — descends from this decision.

McCarthy also coined the term "artificial intelligence." He organized the Dartmouth Summer Research Project on Artificial Intelligence in 1956, where the field was named and the research agenda established. He spent the rest of his career at MIT and Stanford, working on the problem he had named, never quite solving it, watching it solved differently by people who came later.

He was blunt, impatient with bureaucracy, and right about a number of things that were not widely accepted until decades after he said them.

---

## The thread

These four people solved the problem of what computation *is* before computers existed. Lovelace understood the machine's nature before it was built. Church and Turing answered the fundamental question — what can be computed? — before there was hardware to run computations on. McCarthy gave computation a language that expressed its deepest structure.

Every programming language you will read in this course — C, Haskell, Prolog, Assembly — is an answer to the question: *what should the machine be hiding, and what should it make visible?* The answers in this unit span from "almost nothing" (Assembly: the machine is nearly naked) to "almost everything" (Haskell: the machine is a mathematical abstraction). The history of programming languages is the history of programmers arguing about that question.

The argument began with these four people. Their papers are in `06/scratch/`. Read the originals.
