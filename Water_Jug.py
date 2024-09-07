from collections import deque

def water_jug_solver(jug1, jug2, target):
    queue = deque([(0, 0)])
    visited = set([(0, 0)])
    
    while queue:
        state = queue.popleft()
        x, y = state
        
        if x == target or y == target:
            print("Solution found:", state)
            return

        possible_states = [
            (jug1, y), (x, jug2), (0, y), (x, 0),
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),
            (x + min(y, jug1 - x), y - min(y, jug1 - x))
        ]

        for new_state in possible_states:
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)

    print("No solution found.")

jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

print(f"Water Jug Problem: Jug1 Capacity = {jug1_capacity}, Jug2 Capacity = {jug2_capacity}, Target = {target_amount}")
water_jug_solver(jug1_capacity, jug2_capacity, target_amount)


#Output:

# Water Jug Problem: Jug1 Capacity = 4, Jug2 Capacity = 3, Target = 2
# Solution found: (4, 2)