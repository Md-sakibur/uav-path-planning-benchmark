from src.environment import create_environment, is_free_cell, get_neighbors
from src.visualization import plot_environment
from src.planners.dijkstra import run_dijkstra
from src.planners.astar import run_astar
from src.metrics import summarize_results, save_results_to_json


def main():
    grid, start, goal = create_environment(
        rows=20, cols=20, obstacle_ratio=0.2, seed=42
    )

    print("UAV Path Planning Benchmark Project Initialized")
    print("Grid shape:", grid.shape)
    print("Start:", start, "| Free:", is_free_cell(grid, start))
    print("Goal:", goal, "| Free:", is_free_cell(grid, goal))
    print("Obstacle count:", grid.sum())
    print("Neighbors of start:", get_neighbors(
        start, grid.shape[0], grid.shape[1]))

    d_found, d_path, d_path_cost, d_visited_count, d_runtime = run_dijkstra(
        grid,
        start,
        goal,
        get_neighbors_func=get_neighbors,
        is_free_cell_func=is_free_cell,
    )

    a_found, a_path, a_path_cost, a_visited_count, a_runtime = run_astar(
        grid,
        start,
        goal,
        get_neighbors_func=get_neighbors,
        is_free_cell_func=is_free_cell,
    )

    dijkstra_results = summarize_results(
        d_found, d_path, d_path_cost, d_visited_count, d_runtime
    )
    astar_results = summarize_results(
        a_found, a_path, a_path_cost, a_visited_count, a_runtime
    )

    comparison_results = {
        "dijkstra": dijkstra_results,
        "astar": astar_results,
    }

    print("\nDijkstra Results:")
    print(dijkstra_results)

    print("\nA* Results:")
    print(astar_results)

    save_results_to_json(comparison_results,
                         "outputs/logs/dijkstra_astar_comparison.json")

    plot_environment(
        grid,
        start,
        goal,
        path=d_path,
        save_path="outputs/figures/dijkstra_path.png"
    )

    plot_environment(
        grid,
        start,
        goal,
        path=a_path,
        save_path="outputs/figures/astar_path.png"
    )


if __name__ == "__main__":
    main()
