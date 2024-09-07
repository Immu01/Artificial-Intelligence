def is_valid(coloring, node, color, constraints):
    for neighbor in constraints[node]:
        if coloring.get(neighbor) == color:
            return False
    return True

def map_coloring(nodes, colors, constraints):
    coloring = {}
    
    def backtrack(node):
        if node == len(nodes):
            print("Valid Coloring Found:")
            for n in nodes:
                print(f"{n}: {coloring[n]}")
            return True
        
        for color in colors:
            if is_valid(coloring, nodes[node], color, constraints):
                coloring[nodes[node]] = color
                if backtrack(node + 1):
                    return True
                del coloring[nodes[node]]
        
        return False
    
    if not backtrack(0):
        print("No valid coloring found.")

nodes = ['A', 'B', 'C', 'D']
colors = ['Red', 'Green', 'Blue']
constraints = {
    'A': {'B', 'C'},
    'B': {'A', 'D'},
    'C': {'A', 'D'},
    'D': {'B', 'C'}
}

map_coloring(nodes, colors, constraints)


#Output:

# A: Red
# B: Green
# C: Green
# D: Red