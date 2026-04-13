import numpy as np


def create_environment(rows=20, cols=20, obstacle_ratio=0.2, seed=None):
    if seed is not None:
        np.random.seed(seed)

    grid = np.zeros((rows, cols), dtype=int)

    total_cells = rows * cols
    obstacle_count = int(total_cells * obstacle_ratio)

    obstacle_indices = np.random.choice(
        total_cells, obstacle_count, replace=False)

    for idx in obstacle_indices:
        r = idx // cols
        c = idx % cols
        grid[r, c] = 1

    start = (0, 0)
    goal = (rows - 1, cols - 1)

    grid[start] = 0
    grid[goal] = 0

    return grid, start, goal


def is_free_cell(grid, position):
    r, c = position
    return grid[r, c] == 0


def get_neighbors(position, rows, cols):
    r, c = position
    candidates = [
        (r - 1, c),
        (r + 1, c),
        (r, c - 1),
        (r, c + 1),
    ]

    neighbors = []
    for nr, nc in candidates:
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))

    return neighbors
