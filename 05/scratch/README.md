# Scratch — Unit 05: Public Enterprise

Six starting points. Pick the one that pulls you first.

---

## LaTeX — typeset something

Install TeX Live if it isn't present: `sudo pacman -S texlive-basic texlive-latex`

Create `hello.tex`:

```latex
\documentclass{article}
\usepackage{amsmath}
\title{A Small Thing, Typeset Well}
\author{Your Name}
\date{\today}
\begin{document}
\maketitle
Consider the integral $\int_0^\infty e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2}$.
This sentence was typeset by a program Knuth wrote because he found ugly
typesetting intolerable. The version number converges toward $\pi$.
\end{document}
```

Compile it:

```bash
pdflatex hello.tex
```

Open the PDF. Then find `tex.web` in your TeX Live installation (`locate tex.web`) and open it. Read the first 50 lines. You are reading the source of the program that produced the PDF you just opened. The source is a book.

---

## GIMP — write a script

Install GIMP: `sudo pacman -S gimp`

Open GIMP. Go to Filters → Script-Fu → Console. Type:

```scheme
(car (gimp-version))
```

You are in a Scheme REPL inside an image editor. Now:

```scheme
(let* ((image (car (gimp-file-load RUN-NONINTERACTIVE "/path/to/any.jpg" "any.jpg")))
       (drawable (car (gimp-image-get-active-drawable image))))
  (gimp-brightness-contrast drawable 30 -10)
  (gimp-displays-flush)
  (gimp-image-clean-all image))
```

You have just programmed an image editor in Lisp. The plugin API is the same API external plugins use. Your script is architecturally identical to a shipped feature.

---

## Minecraft — read a mod

You don't need Minecraft installed. Find any small Minecraft Fabric mod on GitHub (search "fabric mod simple example"). Clone it. Look at the structure:

```
src/main/java/com/example/yourmod/
├── YourMod.java        ← the entry point
├── mixin/              ← bytecode injection into Minecraft
└── ...
```

The `mixin/` directory is the interesting part. Fabric mods inject code into the closed Minecraft binary by rewriting bytecodes at load time. This is the community working around a closed codebase — legally questionable, technically remarkable. Read one Mixin class and understand what it does.

---

## SageMath — a mathematical session

Install SageMath: `sudo pacman -S sagemath` (or use CoCalc online at cocalc.com — free accounts available).

Start a session:

```bash
sage
```

Try:

```python
# Factor a large number
factor(2^97 - 1)

# Plot something
plot(sin(x) * cos(x), (x, 0, 2*pi))

# Symbolic algebra
x = var('x')
diff(sin(x^2), x)

# Number theory
is_prime(2^61 - 1)
```

Then try something you would normally use Mathematica or MATLAB for. Notice what works. Notice what is different.

The gap between SageMath and a proprietary alternative is not infinite. It is a gap that the community has been closing for twenty years.

---

## SourceForge — the archive

Go to `web.archive.org` and search for `sourceforge.net` between 2001 and 2005. Browse the Wayback Machine captures.

Find a project page for something in this course — GIMP, GDB, Blender's early releases — from that era. Look at the interface. Read the bug tracker. Read the mailing list archives.

This is what open development looked like before GitHub. The project is public. The bugs are public. The arguments are public. Save a screenshot in this directory and write three sentences about what you see.

---

## Pure Data — a patch

Install Pure Data: `sudo pacman -S pd` or `sudo pacman -S purr-data`

Open it. Go to File → New to create a new patch. Place objects with `Ctrl+1`:

1. Place a `[metro 500]` object (a metronome, firing every 500ms)
2. Connect it to a `[bang]` object (a button)  
3. Connect that to a `[osc~ 440]` object (a 440Hz oscillator)
4. Connect the oscillator to a `[dac~]` object (your speakers)
5. Click the toggle connected to `metro` to start

You should hear a tone that turns on and off. This is a program. It is also a performance. The patch you built is the score.

Add an `[hslider]` and connect it to the frequency input of `[osc~]`. Move it while the sound plays. You are now live coding.

Save the patch as `first.pd` in this directory.
