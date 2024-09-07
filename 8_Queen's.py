def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve(board, col + 1):
                return True
            board[i][col] = 0
    return False

def solve_8_queens():
    board = [[0] * 8 for _ in range(8)]
    if solve(board, 0):
        print("Solution for 8-Queen Problem:")
        for row in board:
            print(" ".join("Q" if cell else "." for cell in row))
    else:
        print("No solution found.")

solve_8_queens()


#Output:

# Q . . . . . . .
# . . . . . . Q .
# . . . . Q . . .
# . . . . . . . Q
# . Q . . . . . .
# . . . Q . . . .
# . . . . . Q . .
# . . Q . . . . .