# Quiz — xv6 Book Chapter 0: Operating System Interfaces

---

## Processes and memory

1. `fork()` returns twice. What value does it return in the parent? What value in the child?

2. After `fork()`, if you change a variable in the child, does it change in the parent? Why or why not?

3. What does `exec()` do to the calling process's memory? Does it return?

4. What system call would you use to grow a process's memory at runtime?

---

## File descriptors

5. By convention, what are file descriptors 0, 1, and 2?

6. `read()` returns 0. What does that mean?

7. Why is a newly allocated file descriptor always the lowest-numbered unused one? Why does that matter for I/O redirection?

8. `fork()` copies the file descriptor table. What does `exec()` do to it?

---

## Pipes

9. A pipe gives you two file descriptors. What is each one for?

10. Why must the child close the write end of a pipe before calling `exec()` on a program that reads from it?

11. Name two advantages pipes have over temporary files.

---

## File system

12. What is an inode? How is it different from a filename?

13. What does `unlink()` actually do — when is the file's data freed?

14. Why is `cd` built into the shell itself rather than being an external program?

---

## Design

15. Why are `fork()` and `exec()` separate system calls rather than combined into one? What would be harder if they were combined?
