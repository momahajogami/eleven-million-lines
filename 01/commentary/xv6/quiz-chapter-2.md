# Quiz — xv6 Book Chapter 2: Page Tables

---

## Paging hardware

1. What is a page table entry (PTE)? What two things does it contain?

2. A virtual address on x86 is 32 bits. How does the paging hardware use those bits to find the physical address? (Describe the two-level lookup.)

3. What is a page? How large is one?

4. What do the flags `PTE_P`, `PTE_W`, and `PTE_U` mean?

---

## Process address space

5. Where does a process's user memory start in virtual address space? What is the upper limit, and what constant defines it?

6. Why does xv6 include kernel mappings in every process's page table? What convenience does this provide?

7. xv6 cannot use more than 2 gigabytes of physical memory. Why?

---

## Physical memory allocation

8. How does xv6 track which physical pages are free? Describe the data structure.

9. Why does xv6 call `kinit1` and `kinit2` separately instead of a single `kinit`?

10. What does `kfree` write into every byte of a freed page, and why?

---

## Code: exec

11. What file format do xv6 executables use? What "magic number" does `exec` check for?

12. `exec` allocates a new page table before installing the new program. Why does it wait until the new image is fully prepared before switching?

13. What is the guard page, and what happens if the stack grows into it?

14. Why is argument validation in `exec` security-critical? What could a malicious ELF binary do if `exec` skipped the check `ph.vaddr + ph.memsz >= ph.vaddr`?

---

## The TLB

15. What is the Translation Lookaside Buffer (TLB)? What problem does it solve?

16. When xv6 changes a page table, what must it do to avoid stale TLB entries, and how does it do it?

---

## Design

17. A process's physical memory can be non-contiguous, but its virtual addresses appear contiguous starting at zero. What mechanism makes this possible?
