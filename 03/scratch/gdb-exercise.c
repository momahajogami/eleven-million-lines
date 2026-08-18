/* gdb-exercise.c
 *
 * A small program with a deliberate bug. Your job is to find it using GDB,
 * not by reading the source. Read the source afterward to confirm.
 *
 * Compile:  gcc -g -o gdb-exercise gdb-exercise.c
 * Run:      ./gdb-exercise
 * Debug:    gdb ./gdb-exercise
 *
 * GDB commands you will need:
 *   run              — start the program
 *   break sum_array  — set a breakpoint at the function
 *   next             — step over one line
 *   print i          — print the value of i
 *   print arr[i]     — print an array element
 *   backtrace        — show the call stack
 *   quit             — exit GDB
 */

#include <stdio.h>

#define SIZE 5

int sum_array(int *arr, int n) {
    int total = 0;
    for (int i = 0; i <= n; i++) {   /* bug is here */
        total += arr[i];
    }
    return total;
}

double average(int *arr, int n) {
    return (double)sum_array(arr, n) / n;
}

int main(void) {
    int data[SIZE] = {10, 20, 30, 40, 50};

    printf("Sum:     %d\n", sum_array(data, SIZE));
    printf("Average: %.1f\n", average(data, SIZE));
    printf("Expected sum: 150, expected average: 30.0\n");

    return 0;
}
