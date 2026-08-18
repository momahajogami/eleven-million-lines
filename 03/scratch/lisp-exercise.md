# The Lisp Exercise: Changing Emacs While It Runs

This is Freedom 1 in ten minutes. No C compilation required.

The central architectural fact of Emacs: the C core is a Lisp interpreter. The editing experience — every command, every mode, every behavior — is implemented in Emacs Lisp and loaded at startup. When Emacs is running, you can load new Lisp, replacing functions in the running image. The editor changes. Nothing restarts.

---

## Setup

You need a running Emacs. Either:

- The system Emacs: `emacs -nw`
- Your compiled Emacs from `BUILD-emacs.md`: `src/emacs -nw`

It does not matter which. The Lisp layer is the same.

---

## Exercise 1: Read a real function

In Emacs, type:

```
M-x find-function RET count-words RET
```

Emacs opens `simple.el` and jumps to the definition of `count-words`. Read it. It counts words in a region by moving point forward word by word. The entire implementation is in front of you. This is what Freedom 1 looks like in practice: the tool shows you how it works.

Now look at the function just above it: `count-words--buffer-size`. Notice the naming convention — double dash means "private, not for external use." Emacs Lisp has no enforcement mechanism for this; it is a social convention, documented in the GNU Coding Standards.

---

## Exercise 2: Add something

Copy `simple.el` to this scratch directory:

```bash
cp ~/Documents/university-coding/03/emacs/lisp/simple.el \
   ~/Documents/university-coding/03/scratch/simple-modified.el
```

Open `simple-modified.el` and find `count-words`. Add one line that prints a message when the function runs. Find the `interactive` form — it looks like `(interactive (if ...))` — and add immediately after the opening of the function body:

```elisp
(message "count-words called at %s" (current-time-string))
```

Save the file.

---

## Exercise 3: Load it into the running Emacs

In your running Emacs:

```
M-x load-file RET
```

Navigate to `03/scratch/simple-modified.el` and press Enter.

Now run `M-x count-words` on any buffer. Look at the minibuffer. Your message is there. You replaced a function in the running editor with your version.

No recompile. No restart. The editor changed.

---

## Exercise 4: Go further

The `lisp/play/` directory contains `doctor.el`, `hanoi.el`, `tetris.el`, `bubbles.el`, and others. Pick one. Read it. Find something small to change — a response string in `doctor.el`, the speed of a Hanoi move in `hanoi.el`. Load your modified version. See the change.

---

## What you just did

The standard tool-use relationship: the tool is a fixed artifact. You operate it. You do not change it.

The Emacs relationship: the tool is an environment. You enter it. You change it. The change persists for the life of the session — and if you add your modification to your `~/.emacs.d/init.el`, it persists forever. The tool becomes yours.

This is the architecture Stallman designed. It is not an accident that Emacs works this way. It is a direct expression of the philosophy in the GNU Manifesto: that software should be something users can understand, modify, and share — not a fixed artifact handed down from a vendor.

---

## Reading

- `03/emacs/lisp/simple.el` — foundational Emacs Lisp; 8,000+ lines
- `03/scratch/doctor.el` + `03/scratch/doctor-annotation.md` — the surprise
- The GNU Coding Standards (`03/scratch/gnu-coding-standards.txt`), section on Lisp conventions
