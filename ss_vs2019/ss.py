#!/usr/bin/env python

import sys

# blank used as starting point for entering new puzzle
puzzXX = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],

          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],

          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Daily Sudoku:  Sat 9-Jul-2016
puzz00 = [[0, 0, 7, 0, 0, 5, 9, 6, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 5],
          [0, 3, 0, 0, 7, 0, 0, 0, 4],

          [0, 0, 8, 2, 3, 0, 0, 0, 0],
          [0, 2, 0, 0, 0, 0, 0, 7, 0],
          [0, 0, 0, 0, 8, 9, 6, 0, 0],

          [8, 0, 0, 0, 6, 0, 0, 9, 0],
          [2, 7, 0, 0, 0, 0, 0, 0, 0],
          [0, 4, 9, 3, 0, 0, 1, 0, 0]]

# Daily Sudoku:  Sat 16-Jul-2016
puzz01 = [[0, 0, 7, 9, 0, 0, 0, 0, 4],
          [0, 2, 0, 6, 0, 8, 0, 7, 0],
          [0, 0, 8, 0, 0, 7, 0, 0, 0],

          [0, 0, 1, 0, 0, 0, 0, 0, 3],
          [0, 8, 0, 4, 0, 9, 0, 2, 0],
          [4, 0, 0, 0, 0, 0, 1, 0, 0],

          [0, 0, 0, 7, 0, 0, 6, 0, 0],
          [0, 9, 0, 2, 0, 3, 0, 1, 0],
          [3, 0, 0, 0, 0, 4, 5, 0, 0]]

# Daily Sudoku:  Sat 23-Jul-2016
puzz02 = [[8, 0, 0, 0, 6, 4, 0, 5, 0],
          [2, 0, 4, 0, 1, 0, 0, 3, 6],
          [0, 0, 0, 0, 0, 0, 0, 0, 8],

          [0, 0, 1, 0, 0, 0, 0, 0, 0],
          [9, 5, 0, 0, 0, 0, 0, 2, 3],
          [0, 0, 0, 0, 0, 0, 5, 0, 0],

          [6, 0, 0, 0, 0, 0, 0, 0, 0],
          [7, 8, 0, 0, 4, 0, 6, 0, 1],
          [0, 1, 0, 6, 3, 0, 0, 0, 2]]

# Daily Sudoku:  Sun 14-Aug-2016
puzz03 = [[0, 0, 7, 9, 1, 0, 0, 0, 0],
          [0, 0, 3, 2, 0, 0, 0, 8, 0],
          [0, 8, 1, 6, 0, 0, 0, 5, 0],

          [0, 7, 0, 0, 0, 0, 0, 0, 0],
          [9, 0, 0, 3, 0, 6, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 2, 0],

          [0, 4, 0, 0, 0, 2, 9, 1, 0],
          [0, 1, 0, 0, 0, 9, 5, 0, 0],
          [0, 0, 0, 0, 4, 7, 2, 0, 0]]

# Daily Sudoku:  Sun 8-Aug-2019 (easy)
puzz04 = [[7, 6, 0, 0, 0, 0, 0, 8, 2],
          [0, 0, 0, 0, 5, 0, 0, 0, 0],
          [0, 0, 0, 8, 0, 6, 0, 0, 0],

          [8, 0, 0, 3, 0, 4, 0, 0, 9],
          [0, 0, 9, 0, 7, 0, 8, 0, 0],
          [2, 0, 1, 0, 0, 0, 3, 0, 7],

          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 3, 9, 0, 5, 6, 0, 0],
          [0, 9, 4, 7, 0, 8, 5, 2, 0]]

# Daily Sudoku:  Sat 14-Mar-2020 (medium)
puzz05 = [[0, 0, 0, 8, 0, 3, 0, 6, 0],
          [9, 0, 0, 5, 7, 0, 0, 0, 0],
          [4, 0, 0, 0, 0, 0, 0, 0, 3],

          [0, 5, 0, 0, 0, 0, 3, 0, 0],
          [0, 6, 0, 9, 1, 2, 0, 8, 0],
          [0, 0, 4, 0, 0, 0, 0, 2, 0],

          [7, 0, 0, 0, 0, 0, 0, 0, 8],
          [0, 0, 0, 0, 4, 6, 0, 0, 1],
          [0, 1, 0, 3, 0, 8, 0, 0, 0]]

# Daily Sudoku:  Sat 2-Jul-2021 (easy)
puzz06 = [[5, 9, 0, 0, 0, 1, 7, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 0, 3],
          [0, 0, 3, 0, 4, 0, 0, 0, 9],

          [1, 0, 5, 0, 0, 3, 0, 4, 0],
          [3, 6, 0, 0, 0, 0, 0, 7, 1],
          [0, 8, 0, 1, 0, 0, 2, 0, 5],

          [9, 0, 0, 0, 2, 0, 5, 0, 0],
          [7, 0, 0, 4, 0, 0, 0, 0, 0],
          [0, 0, 1, 7, 0, 0, 0, 9, 2]]

puzzle = puzz06


def print_puzzle():
    for i in range(9):
        if i % 3 == 0:
            print("-------------------------")
        for j in range(9):
            if j % 3 == 0:
                print("|", end=' ')
            if puzzle[i][j] == 0:
                print("_", end = ' ')
            else:
                print(puzzle[i][j], end=' ')
        print("|")
    print("-------------------------")


def get_indexes(_square):
    """
    Returns row, column, and box indexes for a square.
    Indexing is 0-based and goes left-to-right and top-to-bottom.
    0 is the top-left square index, 80 is the bottom-right square index.
    Rows are numbered 0-8 from the top-to-bottom.
    Columns are numbered 0-8 from left-to-right.
    0 is the top-left box index, 8 is the bottom-right box index.

    :param _square: 0-based square index
    :return: (0-based row index, 0-based column index, 0-based box index)
    """
    _row = _square // 9
    _col = _square % 9
    _box = (_col // 3) + ((_row // 3) * 3)
    return _row, _col, _box


if __name__ == "__main__":

    is_solving = True
    moves_stack = []
    guess_ct = 0
    backtrack_ct = 0
    choice_max_ct = 0

    print("THE PUZZLE:")
    print_puzzle()

    while is_solving:

        # start with sets of all possible elements that can occur in each box, row, col
        nbox = [set(range(1, 10)) for _ in range(9)]
        nrow = [set(range(1, 10)) for _ in range(9)]
        ncol = [set(range(1, 10)) for _ in range(9)]

        # whittle those sets down to what's NOT in each box, row, col
        # and also count how many squares are solved
        solved_ct = 0
        for square in range(81):
            row, col, box = get_indexes(square)
            elem = puzzle[row][col]
            if elem != 0:
                # TODO -- maybe handle error here if box data is bad
                nbox[box].remove(elem)
                nrow[row].remove(elem)
                ncol[col].remove(elem)
                solved_ct += 1

        # end if all squares have a solution
        if solved_ct == 81:
            is_solving = False
            break

        # apply membership constraint to rows, columns, and boxes
        new_guesses = []
        is_guess_needed = True
        for square in range(81):
            row, col, box = get_indexes(square)
            elem = puzzle[row][col]
            if elem == 0:
                # this is an unsolved square so find potential solutions
                # solution is intersection of !box and !row and !col
                square_solution = nbox[box] & nrow[row] & ncol[col]
                if len(square_solution) == 0:
                    # solution set is empty
                    # this is a contradiction so a guess was incorrect
                    # pop stuff off stack until a guess is reached
                    # apply new guess and break to begin next iteration
                    while moves_stack:
                        row, col, val, guesses = moves_stack.pop()
                        if len(guesses):
                            # found a move that was a guess
                            # so apply next value in square's solution set as a new guess
                            new_val = guesses.pop()
                            puzzle[row][col] = new_val
                            moves_stack.append((row, col, new_val, guesses))
                            is_guess_needed = False
                            break
                        else:
                            # the move has no more guesses associated with it
                            # so just undo the move
                            puzzle[row][col] = 0
                            backtrack_ct += 1
                    # the above loop should have found a guess and cleared this flag
                    # if it didn't then the puzzle has no solution (I think)
                    if is_guess_needed:
                        print("WTF?")
                        sys.exit(1)
                    break
                elif len(square_solution) == 1:
                    # this is a unique solution for a square
                    # update puzzle and add to stack
                    # break and begin next iteration since
                    # the row, col, box sets need to be reevaluated
                    val = square_solution.pop()
                    puzzle[row][col] = val
                    moves_stack.append((row, col, val, set([])))
                    is_guess_needed = False
                    break
                else:
                    # there are multiple solutions for this square
                    # add its solution set to collection of guesses
                    new_guesses.append((row, col, square_solution))

        if is_guess_needed:
            # the previous constraint check did not make any progress
            # so a guess must be made to continue checking solutions
            # first sort guess list by fewest number of guess choices
            new_guesses.sort(key=lambda x: len(x[2]))

            # each guess set is guaranteed to have a correct choice
            # so just apply the first choice from first guess in list
            # eventually incorrect guesses will get used up
            # as constraint check reveals contradictions
            row, col, guesses = new_guesses[0]
            val = guesses.pop()
            puzzle[row][col] = val
            moves_stack.append((row, col, val, guesses))
            guess_ct += 1

            # update maximum number of choices used for a guess
            if len(new_guesses[0]) > choice_max_ct:
                choice_max_ct = len(new_guesses[0])

    print("SOLUTION:")
    print_puzzle()
    print(f"Guesses:      {guess_ct}")
    print(f"Backtracks:   {backtrack_ct}")
    print(f"Max Choices:  {choice_max_ct}")
