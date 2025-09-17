import random

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def hill_climb(grid, start, goal, max_restarts=5):
    best_path = None
    best_cost = float('inf')
    nodes_expanded = 0

    for _ in range(max_restarts):
        current = start
        path = [current]
        visited = set()
        while current != goal:
            neighbors = grid.get_neighbors(current)
            if not neighbors:
                break
            nodes_expanded += 1
            current = min(neighbors, key=lambda n: heuristic(n, goal))
            if current in visited:
                break
            visited.add(current)
            path.append(current)

        if path[-1] == goal and len(path) < best_cost:
            best_path = path
            best_cost = len(path)

    return (best_path, nodes_expanded) if best_path else (None, nodes_expanded)