import sys
import time
from environment import Grid
from bfs import bfs
from astar import astar
from local_search import hill_climb

def run_algorithm(name, algorithm, grid, start, goal):
    start_time = time.time()
    path, nodes_expanded = algorithm(grid, start, goal)
    end_time = time.time()

    print(f"\n--- {name} on this map ---")
    if path:
        print("Path:", path)
        print("Path length:", len(path))
        print("Nodes expanded:", nodes_expanded)
        print("Execution time: {:.2f} ms".format((end_time - start_time) * 1000))
    else:
        print("No path found")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python src/main.py <bfs|astar|local> <mapfile>")
        sys.exit(1)

    algo = sys.argv[1]
    map_file = sys.argv[2]

    grid = Grid(map_file)
    start, goal = grid.find_points()

    if algo == "bfs":
        run_algorithm("BFS", bfs, grid, start, goal)
    elif algo == "astar":
        run_algorithm("A*", astar, grid, start, goal)
    elif algo == "local":
        run_algorithm("Hill Climbing", hill_climb, grid, start, goal)
    else:
        print("Unknown algorithm:", algo)