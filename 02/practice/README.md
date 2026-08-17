# Practice — Unit 02: Classic C Compilers

This is the working directory. The repos in `02/gcc/` and `02/tcc/` are primary texts — they are not modified. Everything in here is fair game: copy it, change it, break it, rebuild it.

---

## What's here

**`tcc/`** — A working copy of Bellard's Tiny C Compiler. Build it. Read it. Modify it. If you break it beyond recovery, delete the directory and copy again from `02/tcc/`.

**`scratch/`** — Write C programs here to test against the compilers. Small programs; nothing fancy. This is where you put `hello.c`, your test cases, and anything else you want to compile and run.

**`sets/`** — Problem sets and reading exercises, as PDFs and markdown source. Three problem sets (one per commentary document), five reading exercises. The PDFs are generated from the markdown; regenerate with `python3 sets/generate_pdfs.py`.

---

## Quick start

```bash
# Build the practice copy of TCC
cd practice/tcc
./configure && make

# Compile a test program
cd ../scratch
../tcc/tcc hello.c -o hello
./hello

# Or run it directly as a script
../tcc/tcc -run hello.c
```

---

## The rule

The originals in `02/tcc/` and `02/gcc/` do not change. Everything in `practice/` is yours.
