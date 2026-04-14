from src.environment import create_environment, is_free_cell, get_neighbors
from src.visualization import plot_environment
from src.planners.dijkstra import run_dijkstra
from src.metrics import summarize_results, save_results_to_json


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

    found, path, path_cost, visited_count = run_dijkstra(
        grid,
        start,
        goal,
        get_neighbors_func=get_neighbors,
        is_free_cell_func=is_free_cell,
    )

    results = summarize_results(found, path, path_cost, visited_count)

    print("Results summary:")
    print(results)

    save_results_to_json(results, "outputs/logs/dijkstra_results.json")

    plot_environment(
        grid,
        start,
        goal,
        path=path,
        save_path="outputs/figures/dijkstra_path.png"
    )


if __name__ == "__main__":
    main()
