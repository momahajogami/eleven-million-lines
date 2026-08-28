# Quiz — xv6 Book Chapter 3: Traps, Interrupts, and Drivers

---

## The three cases

1. What are the three events that cause control to transfer from a user program to the kernel? Give a concrete example of each.

2. What is the difference between a trap and an interrupt? Why are interrupts harder to reason about?

3. What three things must the operating system do in all three cases (system call, exception, interrupt)?

---

## X86 protection

4. How many protection levels does x86 support? Which two does xv6 use, and what are they called?

5. What is the IDT? How many entries does it have?

6. When a user program invokes `int n`, what does the hardware do — step by step?

7. Why can't the kernel use the user stack when handling a trap?

---

## Assembly trap handlers

8. What is `tvinit()`'s job? Why does xv6 need 256 different entry points rather than one?

9. What is `alltraps`? What does it build on the kernel stack?

10. What is a trap frame? What information does it contain, and why is all of it needed?

11. Why does `tvinit` set the system call gate as a "trap gate" rather than an "interrupt gate"?

---

## The C trap handler

12. What does the C function `trap()` do with the trap frame it receives?

13. If the trap is not a system call and not a hardware interrupt, what does `trap()` conclude, and what does it do?

14. If a trap occurs while the kernel itself is executing (not a user program), what does xv6 do?

---

## System calls

15. How does `syscall()` know which system call to invoke? Where is the system call number stored?

16. What does `syscall()` do with the return value of the system call function?

17. What do `argint`, `argptr`, and `argstr` do, and why can't the kernel simply trust the pointer values a user program passes?

---

## Interrupts and drivers

18. What is a driver?

19. What is the difference between polling (busy waiting) and using interrupts? When is each preferable?

20. What do the flags `B_VALID` and `B_DIRTY` mean in the disk driver?

21. When `iderw` sends a disk request, why does it sleep rather than poll for the result?

22. When the disk finishes an operation, it raises an interrupt. Trace the path: what code runs, in what order, from the interrupt to the process being woken up?
