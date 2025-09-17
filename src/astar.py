import heapq

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    open_set = [(0, start)]
    came_from = {start: None}
    g_score = {start: 0}
    nodes_expanded = 0

    while open_set:
        _, current = heapq.heappop(open_set)
        nodes_expanded += 1

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1], nodes_expanded

        for neighbor in grid.get_neighbors(current):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

    return None, nodes_expanded