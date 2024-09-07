def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" -> ")

    for neighbor in graph[start] - visited:
        dfs(graph, neighbor, visited)

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

print("DFS Traversal Order:")
dfs(graph, 'A')


#Output:

# DFS Traversal Order:
# A -> B -> D -> E -> F -> C -> C -> % 