# xv6 — Entry

*The first walk through. Where to stand, what to look at, what to feel.*

---

## The numbers

9,400 lines of C and assembly. That is an operating system. Process management, virtual memory, a filesystem, a shell, a handful of user programs. Everything required for Unix to exist, in a space smaller than most single files in a modern codebase.

Hold that number. It will keep mattering.

---

## The door: `main.c`

Open `main.c`. It is 38 lines of actual code.

```c
int
main(void)
{
  kinit1(end, P2V(4*1024*1024)); // phys page allocator
  kvmalloc();      // kernel page table
  mpinit();        // detect other processors
  lapicinit();     // interrupt controller
  seginit();       // segment descriptors
  picinit();       // disable pic
  ioapicinit();    // another interrupt controller
  consoleinit();   // console hardware
  uartinit();      // serial port
  pinit();         // process table
  tvinit();        // trap vectors
  binit();         // buffer cache
  fileinit();      // file table
  ideinit();       // disk
  startothers();   // start other processors
  kinit2(P2V(4*1024*1024), P2V(PHYSTOP)); // must come after startothers()
  userinit();      // first user process
  mpmain();        // finish this processor's setup
}
```

You have just read the boot sequence of an operating system. Each line wakes something up — hardware, memory, interrupt handling — in the exact order required. The comments are not documentation appended afterward. They are the code. Each one is a complete sentence describing a complete act.

Notice `userinit()`. That is the moment Unix begins. Everything before it is the kernel making itself ready. Everything after it is the kernel waiting to be interrupted by a user process wanting something. The whole model is there in the call order.

`mpmain()` at the end hands off to the scheduler and never returns. The kernel becomes reactive. That is what an operating system is: a very careful initialization followed by infinite patience.

---

## Five files worth reading in order

These are not the only important files. They are the path in.

### 1. `main.c` — the boot sequence

Already read. 38 lines. Do not skip it.

### 2. `proc.c` — the process model

534 lines. `fork()`, `exit()`, `wait()`, `sleep()`, `wakeup()`, the scheduler. This is the heart of Unix. Every time you run a command in a shell, `fork()` happens. Every time a program finishes, `exit()` and `wait()` happen. Read `fork()` first — it is about 40 lines and it is one of the most important functions ever written.

### 3. `vm.c` — virtual memory

394 lines. How the kernel gives each process the illusion that it owns all of memory. Dense but not long. The key function is `copyuvm()` — it shows what `fork()` actually does to memory when it duplicates a process.

### 4. `fs.c` — the filesystem

670 lines, the longest kernel file. Inodes, directories, path traversal. The filesystem is where Unix becomes a place — where programs and data have names and addresses that persist. Read `namei()` to see how a path like `/usr/bin/grep` becomes an inode.

### 5. `sh.c` — the shell

493 lines. A complete Unix program, not a kernel file. The shell is the user's interface to everything above. It forks processes, sets up pipes, redirects I/O. Reading it after `proc.c` is the payoff: you see `fork()` being used in the wild, doing exactly what it was designed to do.

---

## What the README says

xv6's own README acknowledges Lions' Commentary directly:

> *xv6 is inspired by John Lions's Commentary on UNIX 6th Edition.*

That sentence is not an accident. xv6 was written to be read alongside a commentary. The authors knew they were making a text, not just a program. That is rare. Treat it accordingly.

---

## The moment

You are standing inside a working operating system. It boots. It runs processes. It has a filesystem and a shell. It does everything Unix does. And you can read the whole thing in an afternoon.

That is not a simplification. That is what it actually was — what Thompson and Ritchie actually built, before decades of accumulation. The smallness is not a teaching conceit. The smallness is the original fact.

---

*Next: `proc.c` — read `fork()` and feel the process model click into place.*
