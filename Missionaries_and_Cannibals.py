from collections import deque

def is_valid_state(state):
    m_left, c_left, boat, m_right, c_right = state
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    return True

def get_successors(state):
    m_left, c_left, boat, m_right, c_right = state
    successors = []
    if boat == 1:
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_state = (m_left - m, c_left - c, 0, m_right + m, c_right + c)
            if is_valid_state(new_state):
                successors.append(new_state)
    else:
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_state = (m_left + m, c_left + c, 1, m_right - m, c_right - c)
            if is_valid_state(new_state):
                successors.append(new_state)
    return successors

def solve_missionaries_cannibals():
    initial_state = (3, 3, 1, 0, 0)
    queue = deque([(initial_state, [])])
    visited = set([initial_state])
    
    while queue:
        current_state, path = queue.popleft()
        if current_state == (0, 0, 0, 3, 3):
            print("Solution Found:")
            for step in path + [current_state]:
                print(step)
            return
        
        for successor in get_successors(current_state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [current_state]))
    
    print("No solution found.")

solve_missionaries_cannibals()


#Output:

# Solution Found:
# (3, 3, 1, 0, 0)
# (3, 1, 0, 0, 2)
# (3, 2, 1, 0, 1)
# (3, 0, 0, 0, 3)
# (3, 1, 1, 0, 2)
# (1, 1, 0, 2, 2)
# (2, 2, 1, 1, 1)
# (0, 2, 0, 3, 1)
# (0, 3, 1, 3, 0)
# (0, 1, 0, 3, 2)
# (1, 1, 1, 2, 2)
# (0, 0, 0, 3, 3)