def find_next_empty(puzzle):
    # empty spaces are rep as -1
    # return row, col tuple (None, None if there is none)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c

    return None, None

# checks if guess made is valid
def is_valid(puzzle, guess, row, col):
    
    row_vals = puzzle[row]
    # checks rows
    if guess in row_vals:
        return False
    
    # checks cols
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # now check squares
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True 

def solve_sudoku(puzzle):

    row, col = find_next_empty(puzzle)

    # if row is None then the puzzle has been solved
    if row is None:
        return True

    # make guess if we are not done
    for guess in range(1, 10): # 1-9

        if is_valid(puzzle, guess, row, col):
            # if valid guess then insert it
            puzzle[row][col] = guess
            # recurse through and solve the puzzle
            if solve_sudoku(puzzle):
                return True
        
        # if not valid we will backtrack and try a new number
        puzzle[row][col] = -1

    # return false because the puzzle is unsolvable
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)