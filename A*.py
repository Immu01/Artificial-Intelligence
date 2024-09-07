from heapq import heappop, heappush

def a_star(graph, start, goal, heuristic):
    open_list = [(0, start)]
    g_costs = {start: 0}
    came_from = {}
    
    while open_list:
        _, current = heappop(open_list)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            path.reverse()
            print("Shortest Path:", " -> ".join(path))
            return
        
        for neighbor, cost in graph[current].items():
            tentative_g_cost = g_costs[current] + cost
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current

    print("No path found.")

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 1, 'E': 5},
    'C': {'A': 3, 'F': 2},
    'D': {'B': 1, 'G': 3},
    'E': {'B': 5, 'G': 1},
    'F': {'C': 2, 'G': 1},
    'G': {}
}

heuristic = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3, 'F': 2, 'G': 0}

a_star(graph, 'A', 'G', heuristic)


#Output:

# Shortest Path: A -> B -> D -> G