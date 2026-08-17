# Scratch — Unit 03: Richard Stallman

This directory is for engagement with the tools this unit is about. Nothing here is precious. Write, compile, debug, annotate. Leave notes.

---

## Suggested activities

### 1. Read the GNU Manifesto with a pen

Print or open `gnu.org/gnu/manifesto.html`. Read it slowly. Mark every claim you agree with. Mark every claim that surprises you. Mark every claim you want to argue with.

Then write one paragraph in this directory — call it `manifesto-response.md` — with your honest reaction. Not a summary. A response.

### 2. Read the GPL as a document

Open GPL v2 at `gnu.org/licenses/old-licenses/gpl-2.0.html`. Read it end to end as if it were a short story. Note the section called "Terms and Conditions for Copying, Distribution and Modification." Notice the "liberty or death" clause (section 7). What is it guarding against?

Then open GPL v3. Find the sections on patents and tivoization. What specific threats arrived between 1991 and 2007 that required new language?

Save your notes as `gpl-reading.md`.

### 3. Debug something with GDB

Write a small C program with an intentional bug — an off-by-one error, a null dereference, whatever you like. Save it as `buggy.c`. Compile it:

```bash
gcc -g -o buggy buggy.c
```

Run it under GDB:

```bash
gdb ./buggy
(gdb) break main
(gdb) run
(gdb) next
(gdb) print variable_name
(gdb) backtrace
```

Find the bug in GDB before you look at the source. This is what GDB was built for. It is forty years old and it still works exactly as designed.

### 4. Write one function of Emacs Lisp

Install Emacs if it isn't installed (`sudo pacman -S emacs`). Open it. Press `M-x ielm` to open the Emacs Lisp REPL. Type:

```elisp
(defun hello-gnu ()
  (interactive)
  (message "Hello from a free program in a free editor."))
```

Then run it with `M-x hello-gnu`. You have just extended a running program by writing code inside it. This is Freedom 1 expressed in the act of using the tool.

### 5. Annotate a license

Pick GPL v2 or v3. Copy it into `gpl-annotated.md`. For each section, add a one-sentence plain-English translation. This is harder than it sounds. Do it.
