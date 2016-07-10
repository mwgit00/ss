import sys


# Daily Sudoku:  Sat 9-Jul-2016
puzzle = [[0, 0, 7, 0, 0, 5, 9, 6, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 5],
          [0, 3, 0, 0, 7, 0, 0, 0, 4],

          [0, 0, 8, 2, 3, 0, 0, 0, 0],
          [0, 2, 0, 0, 0, 0, 0, 7, 0],
          [0, 0, 0, 0, 8, 9, 6, 0, 0],

          [8, 0, 0, 0, 6, 0, 0, 9, 0],
          [2, 7, 0, 0, 0, 0, 0, 0, 0],
          [0, 4, 9, 3, 0, 0, 1, 0, 0]]


def print_puzzle():
    for i in range(9):
        if i % 3 == 0:
            print "-------------------------"
        for j in range(9):
            if j % 3 == 0:
                print "|",
            if puzzle[i][j] == 0:
                print "_",
            else:
                print puzzle[i][j],
        print "|"
    print "-------------------------"


if __name__ == "__main__":

    is_solving = True
    moves_stack = []

    print "THE PUZZLE:"
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
            row = square / 9
            col = square % 9
            box_id = (col / 3) + ((row / 3) * 3)
            elem = puzzle[row][col]
            if elem != 0:
                nbox[box_id].remove(elem)
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
            row = square / 9
            col = square % 9
            box_id = (col / 3) + ((row / 3) * 3)
            elem = puzzle[row][col]
            if elem == 0:
                # this is an unsolved square so find potential solutions
                # solution is intersection of !box and !row and !col
                square_solution = nbox[box_id] & nrow[row] & ncol[col]
                if len(square_solution) == 0:
                    # solution set is empty
                    # this is a contradiction so a guess was incorrect
                    # pop stuff off stack until a guess is reached
                    # apply new guess and break to begin next iteration
                    while moves_stack:
                        row, col, val, guesses = moves_stack.pop()
                        if len(guesses):
                            # found a move that was a guess
                            # so apply next value in solution set as a new guess
                            new_val = guesses.pop()
                            puzzle[row][col] = new_val
                            moves_stack.append((row, col, new_val, guesses))
                            is_guess_needed = False
                            break
                        else:
                            # the move has no more guesses associated with it
                            # so just undo the move
                            puzzle[row][col] = 0
                    # the above loop should have found a guess and cleared this flag
                    # if it didn't then the puzzle had no solution (I think)
                    if is_guess_needed:
                        print "WTF?"
                        sys.exit(1)
                    break
                elif len(square_solution) == 1:
                    # this is a unique solution for a square
                    # update puzzle and add to stack
                    # break and begin next iteration
                    val = square_solution.pop()
                    puzzle[row][col] = val
                    moves_stack.append((row, col, val, set([])))
                    is_guess_needed = False
                    break
                else:
                    # multiple solutions for this square
                    # add it to collection of guesses
                    new_guesses.append((row, col, square_solution))

        if is_guess_needed:
            # the following operations did not make any progress
            # sort guesses so those with fewest number of choices are first
            new_guesses.sort(key=lambda x: len(x[2]))

            # find guess that hasn't been made
            # eventually the guesses will get used up
            row, col, guesses = new_guesses[0]
            val = guesses.pop()
            puzzle[row][col] = val
            moves_stack.append((row, col, val, guesses))

    print "SOLUTION:"
    print_puzzle()
