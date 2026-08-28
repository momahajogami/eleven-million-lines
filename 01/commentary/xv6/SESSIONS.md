# xv6 Reading Sessions

---

## 2026-08-27 — main.c and the boot sequence

**What we read:** `01/xv6/main.c`, `01/xv6/initcode.S`, and `01/commentary/xv6/entry.md`

**Key things learned:**

- `main.c` is about 38 lines *through the end of `main()`* — stop at line 38. Lines 40+ are multiprocessor support (`mpenter`, `startothers`, `entrypgdir`) and a separate concern.
- The `main()` function is the boot sequence: each line wakes up one subsystem in the exact order required. The comments *are* the code.
- `userinit()` creates process 1 — the only process the kernel ever creates by hand. Every other process descends from it via `fork()`.
- `mpmain()` at the end calls `scheduler()` and never returns. The kernel becomes reactive. That's what an OS is.
- `initcode.S` is the first user-space program: ~10 lines of assembly that call `exec("/init", argv)` and loop forever calling `exit()` if that fails. It hands off to `/init`, which starts the shell.

**What's next:** Read `proc.c` — specifically `fork()` (~40 lines, one of the most important functions ever written). Then `userinit()` in full. Then the scheduler.

**Resources:** See `01/README.md` — Further reading section.

---

## 2026-08-27 — fork(), copyuvm, and the comonad

**What we read:** `01/xv6/proc.c` (`fork()`, lines 181–222), `01/xv6/vm.c` (`copyuvm()`, lines 316–345)

**Key things learned:**

- `fork()` is ~40 lines. The magic is line 204: `np->tf->eax = 0`. Everything else is copying. That one register write is what makes the child know it's the child — the parent gets `pid` returned, the child gets 0. Same code, two different return values.
- `copyuvm()` walks every page of the parent's address space and physically duplicates it — byte for byte — into fresh pages at the same virtual addresses. The child gets its own real memory, not shared pointers. Expensive and complete.
- **The comonad connection:** A comonad models a *value inseparable from its context* — `extract` lets you peek at the value, but the context is always there, always complete. A process is exactly that: the computation can't be handed to a child without handing it everything — memory, stack, file descriptors, registers. `copyuvm` is the cost of that honesty. The expensiveness of `fork()` isn't a flaw; it's the structure being truthful about what a process is.
- Contrast with a monad: `return`/`pure` *injects* a value into a context — context is added on demand. In a comonad, context is always already present. `extract` just lets you look past it for a moment.

**What's next:** `userinit()` in full, then the scheduler.

---
