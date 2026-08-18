# Building Emacs from Source

This is the Track A exercise: compile GNU Emacs yourself, from the source in `03/emacs/`. It takes 10–20 minutes. At the end you will have an Emacs binary you built, which you can run alongside (or instead of) any system Emacs.

---

## Why bother

You could install Emacs with a package manager in 30 seconds. That is not the point. Building it yourself means you have read the `configure` options, made decisions about what to include, and watched the compiler work through 280 C files. After this, `src/emacs` is yours in a way that `apt install emacs` is not.

This is Freedom 1 at the C level. The Lisp exercise in `lisp-exercise.md` is Freedom 1 at the Lisp level. They are different experiences of the same idea.

---

## Prerequisites (Arch Linux)

```bash
sudo pacman -S base-devel ncurses gnutls libgif libjpeg libpng libtiff libxml2 texinfo
```

For a genuinely minimal build (no graphics, no TLS, terminal only):

```bash
sudo pacman -S base-devel ncurses
```

---

## Step 1: Generate the build system

The Emacs repo does not ship a `configure` script — it ships the files to generate one. From `03/emacs/`:

```bash
cd ~/Documents/university-coding/03/emacs
./autogen.sh
```

This runs autoconf and produces `configure`. Takes about 30 seconds.

---

## Step 2: Configure

Minimal terminal-only build (fastest; good for this exercise):

```bash
./configure \
  --without-x \
  --without-sound \
  --without-dbus \
  --without-gsettings \
  --without-gconf \
  --without-toolkit-scroll-bars \
  --with-x-toolkit=no
```

To see every available option: `./configure --help | less`

The flags we're suppressing are X11 windowing, audio, and desktop integration — none of which you need to read code and run the Lisp exercise. They add build time and dependencies.

---

## Step 3: Compile

```bash
make -j$(nproc)
```

`$(nproc)` uses all your CPU cores. Watch the output: you will see GCC processing each `.c` file in `src/`, then the Lisp files in `lisp/` being byte-compiled. The two phases are visible and distinct.

---

## Step 4: Run

```bash
src/emacs -nw
```

`-nw` means "no window" — forces terminal mode even if X is available. You are now running an Emacs you compiled.

To confirm it is your build and not a system Emacs:

```
M-x emacs-version
```

The path in the output will point to your build directory.

---

## Step 5: Make a change and rebuild

Find a string you can change without breaking anything. A good candidate:

```bash
grep -n "For information about GNU Emacs" lisp/startup.el | head -5
```

Edit that string. Then:

```bash
make -j$(nproc)
src/emacs -nw
```

The change will be there. You changed the program. You compiled it. You ran it. This is the complete cycle.

---

## What the C core does, briefly

`src/` contains ~280 files. The most important:

- `alloc.c` — Emacs' garbage collector and memory allocator
- `eval.c` — the Lisp evaluator
- `buffer.c` — the buffer data structure (everything you edit lives in a buffer)
- `process.c` — subprocess management (how Emacs runs shells, compilers, etc.)
- `keyboard.c` — input handling
- `dispnew.c`, `xdisp.c` — display engine

The C core is a Lisp interpreter. Everything above it — every command, every mode, every behavior — is Lisp. When you understand that, the architecture makes sense.

---

## Troubleshooting

**`./autogen.sh: command not found`** — install `autoconf`: `sudo pacman -S autoconf automake`

**`configure: error: The required function 'tputs' was not found`** — install ncurses: `sudo pacman -S ncurses`

**Build fails partway through** — run `make clean` and try again; partial builds sometimes leave inconsistent state

**`src/emacs` segfaults immediately** — rare; usually a missing library at runtime. Run `ldd src/emacs` to check for missing shared libraries.
