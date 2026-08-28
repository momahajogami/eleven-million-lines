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
