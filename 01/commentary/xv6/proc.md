# xv6 — The Process Model

*The heart. Everything Unix does, it does through this.*

---

## What a process is

A process is the kernel's fiction of a running program. It is not a program — the program is bytes on disk. A process is what the kernel invents to give a program the illusion that it owns a CPU, owns all of memory, owns its own open files. The kernel maintains this fiction for every running program simultaneously.

In xv6, all processes live in a single table:

```c
struct {
  struct spinlock lock;
  struct proc proc[NPROC];
} ptable;
```

Sixty-four slots. That is the maximum number of processes xv6 can run at once. Each slot is a `struct proc` — a record of everything the kernel needs to know about one process: its memory, its stack, its open files, its parent, its state.

The state field is the process's whole biography compressed into one word: `UNUSED`, `EMBRYO`, `SLEEPING`, `RUNNABLE`, `RUNNING`, `ZOMBIE`. A process moves through those states in order, and the scheduler's entire job is watching for `RUNNABLE` and doing something about it.

---

## `fork()` — the most important function ever written

Open `proc.c` and find `fork()` at line 181. It is 42 lines. Read it slowly.

```c
int
fork(void)
{
  int i, pid;
  struct proc *np;
  struct proc *curproc = myproc();

  // Allocate process.
  if((np = allocproc()) == 0){
    return -1;
  }

  // Copy process state from proc.
  if((np->pgdir = copyuvm(curproc->pgdir, curproc->sz)) == 0){
    kfree(np->kstack);
    np->kstack = 0;
    np->state = UNUSED;
    return -1;
  }
  np->sz = curproc->sz;
  np->parent = curproc;
  *np->tf = *curproc->tf;

  // Clear %eax so that fork returns 0 in the child.
  np->tf->eax = 0;

  for(i = 0; i < NOFILE; i++)
    if(curproc->ofile[i])
      np->ofile[i] = filedup(curproc->ofile[i]);
  np->cwd = idup(curproc->cwd);

  safestrcpy(np->name, curproc->name, sizeof(curproc->name));

  pid = np->pid;

  acquire(&ptable.lock);

  np->state = RUNNABLE;

  release(&ptable.lock);

  return pid;
}
```

Here is what is happening, line by line in spirit:

1. **Allocate a new process slot** — `allocproc()` finds an `UNUSED` entry in the process table and sets up a kernel stack and execution context for it.
2. **Copy all of memory** — `copyuvm()` duplicates the parent's entire page directory. The child gets its own copy of every page the parent had. This is expensive; later systems invent copy-on-write to defer it. Here it is done honestly.
3. **Copy the trap frame** — `*np->tf = *curproc->tf` copies the CPU state at the moment of the system call: registers, instruction pointer, stack pointer. The child will resume from exactly the same point as the parent.
4. **Set `%eax` to zero in the child** — this is the answer to the classic interview question. `fork()` returns twice: once in the parent (returning the child's pid) and once in the child (returning 0). The difference is this single line. `%eax` is the return value register on x86. The parent's return value is set at the bottom of the function. The child's is set here, by zeroing the register in the trap frame before the child ever runs.
5. **Duplicate open files and working directory** — the child inherits the parent's file descriptors. This is not a copy of the file data; it is a shared reference to the same open file descriptions. This is how pipes work: parent and child hold handles to the same pipe.
6. **Mark `RUNNABLE`** — the child is now eligible to be scheduled. From this point forward, the scheduler may run it at any time.

The function then returns the child's pid to the parent. The child, when it eventually runs, will return from the same system call with `%eax = 0`.

One function. One call. Two running processes, diverging from the same point.

---

## `exit()` and `wait()` — the other half

`fork()` creates. `exit()` and `wait()` complete the contract.

`exit()` (line 228) does not free the process. It closes files, releases the working directory, wakes the parent, re-parents any children to `init`, and then sets its own state to `ZOMBIE`. A zombie is a process that has finished but whose resources have not yet been reclaimed — because the kernel needs to hold them until the parent comes to collect the exit status.

`wait()` (line 273) is the parent coming to collect. It scans the process table for children in `ZOMBIE` state, frees their resources, and returns the pid. If no children have exited yet, it sleeps — releasing the CPU until one does.

The zombie state exists because of this handshake. Without it, the kernel could free a child's resources before the parent asked for the exit status, and the information would be gone. The zombie waits, frozen, for the parent to acknowledge it.

If a parent exits before its children, `exit()` re-parents those children to `init`. `init` runs an infinite loop calling `wait()`, so orphaned processes always have someone to reap them. This is why `init` cannot itself exit — xv6 panics if it tries.

---

## The scheduler

The scheduler (line 323) is a loop that never returns:

```c
for(;;){
  sti();
  acquire(&ptable.lock);
  for(p = ptable.proc; p < &ptable.proc[NPROC]; p++){
    if(p->state != RUNNABLE)
      continue;
    c->proc = p;
    switchuvm(p);
    p->state = RUNNING;
    swtch(&(c->scheduler), p->context);
    switchkvm();
    c->proc = 0;
  }
  release(&ptable.lock);
}
```

It scans the process table. It finds the first `RUNNABLE` process. It switches to that process's page table (`switchuvm`), marks it `RUNNING`, and then — this is the key — calls `swtch()`, which saves the scheduler's own registers and loads the process's saved registers. The CPU is now running the process.

The scheduler does not run the process. The scheduler *becomes* the process, by swapping register contexts. When the process later yields or blocks, it calls `sched()`, which calls `swtch()` back in the other direction, and the scheduler resumes from the line after its own `swtch()` call.

This is a round-robin scheduler. First fit, no priorities, no fairness guarantees beyond simple rotation. It is the simplest scheduler that works, and it is enough to understand what a scheduler is.

`mpmain()` in `main.c` calls `scheduler()` and never returns. The kernel's initialization thread becomes the scheduler. From that moment on, the kernel has no thread of its own — it exists only in the spaces between processes.

---

## The shape of it

The process model is:
- A table of slots, each holding a process's full state
- `fork()` to copy a slot and diverge
- `exit()` to finish and become a zombie
- `wait()` to reap a zombie and complete the contract
- A scheduler that loops forever, handing the CPU to whoever is ready

Everything else in Unix — shells, pipes, the way programs are launched, the way daemons run, the way signals work — is built on top of this. When you type a command in a shell, the shell calls `fork()`. The child calls `exec()` to replace itself with the command. The parent calls `wait()`. That three-step sequence — fork, exec, wait — is the Unix process model in operation. It is all here.

---

*Next: `vm.c` — how `copyuvm()` actually works, and what it means to give each process its own memory.*
