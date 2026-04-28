# UAV Path Planning Benchmark

## Overview
This project is a Python-based benchmark for comparing classical path planning algorithms for UAV navigation in grid-based obstacle environments.

The project currently implements:
- Dijkstra
- A*

The environment is generated as a 2D grid with random obstacles, a start point, and a goal point. The algorithms are evaluated using path quality and search-efficiency metrics.

---

## Features
- Random 2D grid environment generation
- Obstacle-based path planning
- Start and goal validation
- Environment visualization
- Path visualization
- Dijkstra implementation
- A* implementation
- Multi-seed experiment pipeline
- JSON-based result logging
- Comparison chart for average visited nodes

---

## Implemented Algorithms

### Dijkstra
Dijkstra explores nodes based only on the real cost from the start node.

### A*
A* uses both:
- real cost from the start (`g_cost`)
- estimated cost to the goal (`heuristic`)

This helps A* search more efficiently than Dijkstra in the current benchmark.

---

## Current Results

### Single-map comparison
For the 20x20 environment with obstacle ratio 0.2 and seed 42:

- Dijkstra:
  - path found: True
  - path length: 39
  - path cost: 38
  - visited nodes: 317

- A*:
  - path found: True
  - path length: 39
  - path cost: 38
  - visited nodes: 227

### Multi-seed comparison
Across 5 randomized environments:

- Dijkstra average:
  - total runs: 5
  - success count: 5
  - average path length: 39.0
  - average path cost: 38.0
  - average visited nodes: 318.4

- A* average:
  - total runs: 5
  - success count: 5
  - average path length: 39.0
  - average path cost: 38.0
  - average visited nodes: 187.4

### Key Conclusion
Both Dijkstra and A* achieved the same path quality and 100% success rate in the tested benchmark, but A* required significantly fewer visited nodes, showing better search efficiency.

### Key Conclusion
Both Dijkstra and A* achieved the same path quality and 100% success rate in the tested benchmark, but A* required significantly fewer visited nodes, showing better search efficiency.

## Example Figures

### A* Path Example
![A* Path Example](outputs/figures/astar_path.png)

### Average Visited Nodes Comparison
![Average Visited Nodes Comparison](outputs/figures/dijkstra_astar_average_visited_nodes.png)

---

## Project Structure

```text
uav-path-planning-benchmark/
│
├── README.md
├── requirements.txt
├── main.py
├── .gitignore
│
├── src/
│   ├── environment.py
│   ├── visualization.py
│   ├── metrics.py
│   └── planners/
│       ├── __init__.py
│       ├── dijkstra.py
│       └── astar.py
│
├── experiments/
│   └── basic_test.py
│
├── outputs/
│   ├── figures/
│   └── logs/
│
└── notes/