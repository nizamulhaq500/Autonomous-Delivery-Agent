from collections import deque

def bfs(grid, start, goal):
    queue = deque([start])
    visited = {start: None}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = visited[current]
            return path[::-1], nodes_expanded

        for neighbor in grid.get_neighbors(current):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)

    return None, nodes_expanded