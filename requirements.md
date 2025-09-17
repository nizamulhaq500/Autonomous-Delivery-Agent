# Requirements

This project requires the following environment setup:

## Software
- Python 3.8 or higher

## Libraries
- Standard Python libraries only (no external dependencies):
  - `time`
  - `heapq`
  - `collections`
  - `random`
  - `sys`

## Hardware
- Any modern computer with Python installed
- Minimum 4 GB RAM (for larger maps)

## How to Run
Navigate to the project root directory and execute:

```bash
python src/main.py <algorithm> <mapfile>

Examples:

python src/main.py bfs maps/map_small.txt
python src/main.py astar maps/map_medium.txt
python src/main.py local maps/map_large.txt

