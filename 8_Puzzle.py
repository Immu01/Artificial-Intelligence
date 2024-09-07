import heapq

class Puzzle:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.empty_pos = [(r, c) for r in range(3) for c in range(3) if board[r][c] == 0][0]

    def is_solved(self):
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def possible_moves(self):
        r, c = self.empty_pos
        shifts = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        moves = []
        for dr, dc in shifts:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_board = [row[:] for row in self.board]
                new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
                moves.append(Puzzle(new_board, self.moves + 1, self))
        return moves

    def __lt__(self, other):
        return self.moves + self.manhattan_distance() < other.moves + other.manhattan_distance()

    def manhattan_distance(self):
        distance = 0
        for r in range(3):
            for c in range(3):
                value = self.board[r][c]
                if value != 0:
                    target_r, target_c = (value - 1) // 3, (value - 1) % 3
                    distance += abs(r - target_r) + abs(c - target_c)
        return distance

def solve_puzzle(initial_board):
    initial_state = Puzzle(initial_board)
    queue = []
    heapq.heappush(queue, initial_state)
    visited = set()
    while queue:
        current_state = heapq.heappop(queue)
        if current_state.is_solved():
            return current_state
        visited.add(tuple(map(tuple, current_state.board)))
        for move in current_state.possible_moves():
            if tuple(map(tuple, move.board)) not in visited:
                heapq.heappush(queue, move)
    return None

def print_solution(solution):
    steps = []
    while solution:
        steps.append(solution.board)
        solution = solution.previous
    steps.reverse()
    print("Solution in {} moves:".format(len(steps) - 1))
    for step in steps:
        for row in step:
            print(" ".join(str(num) if num != 0 else " " for num in row))
        print()

initial_board = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
solution = solve_puzzle(initial_board)

if solution:
    print_solution(solution)
else:
    print("No solution found.")


#Output:

# Solution in 2 moves:
# 1 2 3
# 4   5
# 7 8 6

# 1 2 3
# 4 5  
# 7 8 6

# 1 2 3
# 4 5 6
# 7 8  