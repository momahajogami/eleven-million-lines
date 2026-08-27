#!/usr/bin/env python3
"""
Tetris — a readable implementation for Unit 09.

Pajitnov's original insight: seven shapes, one grid, one question.
Can you impose order on entropy before the column fills?

Run with: python3 tetris.py
Controls: a/d move, s drop, w rotate, q quit
"""

import curses
import random
import time

# The seven tetrominoes, each as a list of (row, col) offsets from origin.
# Rotation is handled by transforming these offsets.
PIECES = {
    'I': [(0,0),(0,1),(0,2),(0,3)],
    'O': [(0,0),(0,1),(1,0),(1,1)],
    'T': [(0,0),(0,1),(0,2),(1,1)],
    'S': [(0,1),(0,2),(1,0),(1,1)],
    'Z': [(0,0),(0,1),(1,1),(1,2)],
    'J': [(0,0),(1,0),(1,1),(1,2)],
    'L': [(0,2),(1,0),(1,1),(1,2)],
}

BOARD_ROWS = 20
BOARD_COLS = 10

def empty_board():
    return [[0] * BOARD_COLS for _ in range(BOARD_ROWS)]

def rotate(cells):
    """Rotate 90 degrees clockwise: (r, c) → (c, -r), then normalize to origin."""
    rotated = [(c, -r) for r, c in cells]
    min_r = min(r for r, _ in rotated)
    min_c = min(c for _, c in rotated)
    return [(r - min_r, c - min_c) for r, c in rotated]

def fits(board, cells, row, col):
    for r, c in cells:
        nr, nc = row + r, col + c
        if nr < 0 or nr >= BOARD_ROWS or nc < 0 or nc >= BOARD_COLS:
            return False
        if board[nr][nc]:
            return False
    return True

def place(board, cells, row, col, value=1):
    for r, c in cells:
        board[row + r][col + c] = value

def clear_lines(board):
    full = [r for r in range(BOARD_ROWS) if all(board[r])]
    for r in full:
        board.pop(r)
        board.insert(0, [0] * BOARD_COLS)
    return len(full)

def new_piece():
    name = random.choice(list(PIECES.keys()))
    cells = PIECES[name][:]
    col = BOARD_COLS // 2 - 2
    return cells, 0, col

def draw(stdscr, board, cells, row, col, score):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    # Draw border
    for r in range(BOARD_ROWS + 2):
        stdscr.addch(r, 0, '|')
        stdscr.addch(r, BOARD_COLS * 2 + 1, '|')
    stdscr.addstr(0, 0, '+' + '-' * (BOARD_COLS * 2) + '+')
    stdscr.addstr(BOARD_ROWS + 1, 0, '+' + '-' * (BOARD_COLS * 2) + '+')

    # Draw placed cells
    for r in range(BOARD_ROWS):
        for c in range(BOARD_COLS):
            if board[r][c]:
                stdscr.addstr(r + 1, c * 2 + 1, '[]')

    # Draw falling piece
    for r, c in cells:
        nr, nc = row + r, col + c
        if 0 <= nr < BOARD_ROWS:
            stdscr.addstr(nr + 1, nc * 2 + 1, '[]')

    stdscr.addstr(2, BOARD_COLS * 2 + 4, f'Score: {score}')
    stdscr.addstr(4, BOARD_COLS * 2 + 4, 'a/d  move')
    stdscr.addstr(5, BOARD_COLS * 2 + 4, 'w    rotate')
    stdscr.addstr(6, BOARD_COLS * 2 + 4, 's    drop')
    stdscr.addstr(7, BOARD_COLS * 2 + 4, 'q    quit')
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    board = empty_board()
    cells, row, col = new_piece()
    score = 0
    last_drop = time.time()
    drop_interval = 0.5

    while True:
        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == ord('a'):
            if fits(board, cells, row, col - 1):
                col -= 1
        elif key == ord('d'):
            if fits(board, cells, row, col + 1):
                col += 1
        elif key == ord('w'):
            rotated = rotate(cells)
            if fits(board, rotated, row, col):
                cells = rotated
        elif key == ord('s'):
            while fits(board, cells, row + 1, col):
                row += 1

        # Gravity
        if time.time() - last_drop > drop_interval:
            if fits(board, cells, row + 1, col):
                row += 1
            else:
                place(board, cells, row, col)
                score += clear_lines(board) * 100
                cells, row, col = new_piece()
                if not fits(board, cells, row, col):
                    break  # game over
            last_drop = time.time()

        draw(stdscr, board, cells, row, col, score)
        time.sleep(0.05)

    stdscr.nodelay(False)
    stdscr.addstr(10, 5, f'Game over. Score: {score}. Press any key.')
    stdscr.getch()

if __name__ == '__main__':
    curses.wrapper(main)
