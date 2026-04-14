from src.environment import create_environment, is_free_cell, get_neighbors
from src.planners.dijkstra import run_dijkstra
from src.metrics import summarize_results, save_results_to_json


def compute_average_results(all_results):
    total_runs = len(all_results)
    success_count = sum(1 for result in all_results if result["path_found"])

    average_path_length = sum(result["path_length"]
                              for result in all_results) / total_runs
    average_path_cost = sum(result["path_cost"]
                            for result in all_results) / total_runs
    average_visited_nodes = sum(result["visited_nodes"]
                                for result in all_results) / total_runs

    return {
        "total_runs": total_runs,
        "success_count": success_count,
        "average_path_length": average_path_length,
        "average_path_cost": average_path_cost,
        "average_visited_nodes": average_visited_nodes,
    }


def run_multiple_seeds():
    seeds = [1, 2, 3, 4, 5]
    all_results = []

    for seed in seeds:
        grid, start, goal = create_environment(
            rows=20,
            cols=20,
            obstacle_ratio=0.2,
            seed=seed
        )

        found, path, path_cost, visited_count = run_dijkstra(
            grid,
            start,
            goal,
            get_neighbors_func=get_neighbors,
            is_free_cell_func=is_free_cell,
        )

        result = summarize_results(found, path, path_cost, visited_count)
        result["seed"] = seed
        all_results.append(result)

        print(f"Seed {seed}: {result}")

    summary = compute_average_results(all_results)

    print("\nAverage summary:")
    print(summary)

    save_results_to_json(
        all_results, "outputs/logs/dijkstra_multiple_seeds.json")
    save_results_to_json(summary, "outputs/logs/dijkstra_average_summary.json")


if __name__ == "__main__":
    run_multiple_seeds()
