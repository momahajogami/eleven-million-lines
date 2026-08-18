# doctor.el — The Surprise

Richard Stallman built a psychoanalyst into his text editor.

To run it: open Emacs, type `M-x doctor`. The editor will greet you and begin asking questions. It listens. It reflects. It misunderstands you in exactly the ways a bad therapist misunderstands you. It has been doing this since the 1980s.

---

## What ELIZA was

In 1966, Joseph Weizenbaum at MIT wrote ELIZA — a program that simulated conversation by applying pattern-matching rules to user input and reflecting the language back. The most famous script was DOCTOR, which mimicked a Rogerian psychotherapist. Weizenbaum was disturbed by how readily people formed emotional attachments to ELIZA even knowing it was a program. He wrote about this in *Computer Power and Human Reason* (1976), one of the early books arguing that computers should not be given roles that require genuine human understanding.

Stallman wrote his own ELIZA for the MIT AI Lab's ITS operating system in the late 1970s, and it became part of GNU Emacs from the beginning.

---

## Why it matters for this unit

The canonical image of Stallman is the GPL enforcer: precise, legalistic, unwilling to compromise on principle. `doctor.el` is something else. It is playful. It is weird. It is a 1,654-line Lisp program that asks you how you feel.

Read `doctor.el` as a Lisp program, not as a joke. Notice:

- The pattern-matching rules that recognize keywords ("mother", "dream", "hate") and route responses
- The way it builds up conversational state across an exchange
- The Lisp idioms: `cond`, `assoc`, `mapcar`, `let`

This is idiomatic Emacs Lisp from the 1980s. The style is Stallman's. The humor — deadpan, slightly absurdist — is also Stallman's.

---

## The connection to Freedom 1

`doctor.el` exists because Emacs Lisp is free and Emacs is extensible. Anyone can read it, modify it, distribute a funnier version. Weizenbaum's original ELIZA source was not widely available. Stallman's version has been in the hands of every Emacs user for forty years.

The frivolous and the serious are not separate. The freedom to write a psychoanalyst into your editor is the same freedom that lets you fix a printer driver, modify GCC's optimizer, or fork an entire operating system.

---

## How to read it

Start at the bottom: look for `(defun doctor ...)` — the entry point. Work upward. The data structures (the pattern lists, the response tables) are defined at the top. The logic is in the middle.

Then run it. `M-x doctor`. Tell it something real. Notice what it gets wrong. Then find the rule it used to get it wrong. That gap — between what the program knows and what you meant — is what Weizenbaum was writing about in 1976.
