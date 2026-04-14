from src.environment import create_environment, is_free_cell, get_neighbors
from src.visualization import plot_environment


def main():
    grid, start, goal = create_environment(
        rows=20, cols=20, obstacle_ratio=0.2, seed=42)

    print("UAV Path Planning Benchmark Project Initialized")
    print("Grid shape:", grid.shape)
    print("Start:", start, "| Free:", is_free_cell(grid, start))
    print("Goal:", goal, "| Free:", is_free_cell(grid, goal))
    print("Obstacle count:", grid.sum())
    print("Neighbors of start:", get_neighbors(
        start, grid.shape[0], grid.shape[1]))

    plot_environment(
        grid,
        start,
        goal,
        save_path="outputs/figures/environment.png"
    )


if __name__ == "__main__":
    main()
