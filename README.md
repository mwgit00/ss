# ss

This is my Sudoku Solver.  There are many like it, but this one is mine.

It uses the most basic Sudoku constraint:  no duplicated digits 1-9 in a row, column, or box.  This often leads to several different choices for a square.  The algorithm makes a guess, pushes it on a stack, and keeps going.  When it finds a contradiction, it backtracks and applies a new guess.

I've tested it with a few different puzzles and it seems to work okay.
