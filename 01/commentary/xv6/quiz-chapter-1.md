# Quiz — xv6 Book Chapter 1: Operating System Organization

---

## The three requirements

1. What are the three requirements an operating system must fulfill? Briefly define each one.

2. Why is "complete isolation" too strong a requirement? What would be lost?

---

## Kernel organization

3. What is a monolithic kernel? What is the main advantage of this design?

4. What is the main danger of a monolithic kernel — what happens when it makes a mistake?

5. What is a microkernel? How does it reduce this risk?

6. Which design does xv6 use?

---

## User mode, kernel mode, and system calls

7. What is the difference between kernel mode and user mode on x86?

8. What are "privileged instructions"? Give one example.

9. When a user program makes a system call, what happens at the hardware level?

10. Why is it important that the *kernel* sets the entry point for transitions to kernel mode — not the application?

---

## Process overview

11. A process has two stacks. What are they, and when is each one in use?

12. What does `p->state` record? What does `p->pgdir` hold?

13. Why does xv6 map the kernel into the address space of every user process?

---

## The boot sequence and first process

14. What does the boot loader do? Where does it load the xv6 kernel in physical memory, and why not at `0x0`?

15. What does `allocproc()` do? Why is it used for both `userinit()` and ordinary `fork()`?

16. After `userinit()` sets `p->state = RUNNABLE`, what happens next in the sequence that gets the first process actually running?

17. `userinit()` sets `p->tf->eip = 0`. What is at virtual address 0 in the first process's address space?
