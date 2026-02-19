# Example Sudoku board (0 = empty)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Stack to store positions
stack = []
row = 0
col = 0

while row < 9:
    if board[row][col] == 0:
        found = False
        for num in range(1, 10):
            valid = True

            # Check row
            for i in range(9):
                if board[row][i] == num:
                    valid = False

            # Check column
            for i in range(9):
                if board[i][col] == num:
                    valid = False

            # Check 3x3 box
            start_row = row - row % 3
            start_col = col - col % 3
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        valid = False

            if valid:
                board[row][col] = num
                stack.append((row, col))
                found = True
                break

        if not found:
            board[row][col] = 0
            if stack:
                row, col = stack.pop()
                board[row][col] += 1
                continue
            else:
                print("No solution exists")
                break

    col += 1
    if col == 9:
        col = 0
        row += 1

# Print solved board
print("Solved Sudoku:")
for r in board:
    print(r)
