from src.environment import create_environment, is_free_cell, get_neighbors
from src.visualization import plot_environment
from src.planners.dijkstra import run_dijkstra


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

    found, path = run_dijkstra(
        grid,
        start,
        goal,
        get_neighbors_func=get_neighbors,
        is_free_cell_func=is_free_cell,
    )

    print("Path found:", found)
    print("Path length:", len(path))

    plot_environment(
        grid,
        start,
        goal,
        path=path,
        save_path="outputs/figures/dijkstra_path.png"
    )


if __name__ == "__main__":
    main()
