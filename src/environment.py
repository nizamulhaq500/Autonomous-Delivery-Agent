class Grid:
    def __init__(self, filename):
        self.grid = []
        with open(filename, 'r') as f:
            for line in f:
                self.grid.append(list(line.strip()))

    def get_neighbors(self, pos):
        (x, y) = pos
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0]) and self.grid[nx][ny] != 'X':
                neighbors.append((nx, ny))
        return neighbors

    def find_points(self):
        start = goal = None
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 'S':
                    start = (i, j)
                elif self.grid[i][j] == 'G':
                    goal = (i, j)
        return start, goal