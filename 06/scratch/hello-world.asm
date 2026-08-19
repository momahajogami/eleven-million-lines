; hello-world.asm — "Hello, World" in x86-64 assembly (Linux, NASM syntax)
;
; Assemble and link:
;   nasm -f elf64 hello-world.asm -o hello-world.o
;   ld hello-world.o -o hello-world
;   ./hello-world
;
; What is happening here:
;   - We are making two system calls directly to the Linux kernel
;   - sys_write (syscall number 1): write bytes to a file descriptor
;   - sys_exit  (syscall number 60): terminate the process
;   - Arguments go in registers: rdi, rsi, rdx, r10, r8, r9 (in order)
;   - The syscall instruction transfers control to the kernel
;
; There is no standard library. No printf. No runtime.
; This is the machine talking to the kernel, nothing in between.

section .data
    msg     db  "Hello, World", 10   ; the string, 10 = newline
    msglen  equ $ - msg              ; length = current address minus start

section .text
    global _start

_start:
    ; sys_write(fd=1, buf=msg, count=msglen)
    mov     rax, 1          ; syscall number: sys_write
    mov     rdi, 1          ; file descriptor: 1 = stdout
    mov     rsi, msg        ; pointer to string
    mov     rdx, msglen     ; number of bytes
    syscall

    ; sys_exit(status=0)
    mov     rax, 60         ; syscall number: sys_exit
    mov     rdi, 0          ; exit status: 0 = success
    syscall
