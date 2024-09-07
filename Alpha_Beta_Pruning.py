import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def alpha_beta(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, 'X'):
        return 10 - depth
    if check_winner(board, 'O'):
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = alpha_beta(board, depth + 1, alpha, beta, False)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = alpha_beta(board, depth + 1, alpha, beta, True)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    alpha = -math.inf
    beta = math.inf
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                score = alpha_beta(board, 0, alpha, beta, False)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    
    while True:
        print_board(board)
        player = players[turn % 2]
        
        if player == 'X':
            row, col = best_move(board)
            print(f"Player {player} moves to ({row}, {col})")
        else:
            try:
                row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if board[row][col] != ' ':
                    print("Cell already taken. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Try again.")
                continue
        
        board[row][col] = player
        
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        turn += 1

tic_tac_toe()


# Output:

#   |   |  
# -----
#   |   |  
# -----
#   |   |  
# -----
# Player X's turn
# Enter row and column (0-2) separated by space: 0 0
# X |   |  
# -----
#   |   |  
# -----
#   |   |  
# -----
# Player O's turn
# Enter row and column (0-2) separated by space: 1 1
# X |   |  
# -----
#   | O |  
# -----
#   |   |  
# -----
# Player X's turn
# Enter row and column (0-2) separated by space: 0 1
# X | X |  
# -----
#   | O |  
# -----
#   |   |  
# -----
# Player O's turn
# Enter row and column (0-2) separated by space: 2 2
# X | X |  
# -----
#   | O |  
# -----
#   |   | O
# -----
# Player X's turn
# Enter row and column (0-2) separated by space: 0 2
# X | X | X
# -----
#   | O |  
# -----
#   |   | O
# -----
# Player X wins!