import matplotlib.pyplot as plt

from src.environment import create_environment, is_free_cell, get_neighbors
from src.planners.dijkstra import run_dijkstra
from src.planners.astar import run_astar
from src.metrics import save_results_to_json


def compute_average_results(all_results):
    total_runs = len(all_results)
    success_count = sum(1 for result in all_results if result["path_found"])

    average_path_length = sum(result["path_length"]
                              for result in all_results) / total_runs
    average_path_cost = sum(result["path_cost"]
                            for result in all_results) / total_runs
    average_visited_nodes = sum(result["visited_nodes"]
                                for result in all_results) / total_runs
    average_runtime_seconds = sum(
        result["runtime_seconds"] for result in all_results) / total_runs

    return {
        "total_runs": total_runs,
        "success_count": success_count,
        "average_path_length": average_path_length,
        "average_path_cost": average_path_cost,
        "average_visited_nodes": average_visited_nodes,
        "average_runtime_seconds": average_runtime_seconds,
    }


def plot_average_visited_nodes(dijkstra_average, astar_average, save_path):
    algorithms = ["Dijkstra", "A*"]
    average_visited_nodes = [
        dijkstra_average["average_visited_nodes"],
        astar_average["average_visited_nodes"],
    ]

    plt.figure(figsize=(8, 6))
    plt.bar(algorithms, average_visited_nodes)
    plt.title("Average Visited Nodes: Dijkstra vs A*")
    plt.ylabel("Average Visited Nodes")
    plt.savefig(save_path, bbox_inches="tight")
    plt.show()


def plot_average_runtime(dijkstra_average, astar_average, save_path):
    algorithms = ["Dijkstra", "A*"]
    average_runtime_seconds = [
        dijkstra_average["average_runtime_seconds"],
        astar_average["average_runtime_seconds"],
    ]

    plt.figure(figsize=(8, 6))
    plt.bar(algorithms, average_runtime_seconds)
    plt.title("Average Runtime: Dijkstra vs A*")
    plt.ylabel("Average Runtime (seconds)")
    plt.savefig(save_path, bbox_inches="tight")
    plt.show()


def run_comparison_multiple_seeds():
    seeds = [1, 2, 3, 4, 5]

    dijkstra_results = []
    astar_results = []

    for seed in seeds:
        grid, start, goal = create_environment(
            rows=20,
            cols=20,
            obstacle_ratio=0.2,
            seed=seed
        )

        d_found, d_path, d_path_cost, d_visited, d_runtime = run_dijkstra(
            grid,
            start,
            goal,
            get_neighbors_func=get_neighbors,
            is_free_cell_func=is_free_cell,
        )

        a_found, a_path, a_path_cost, a_visited, a_runtime = run_astar(
            grid,
            start,
            goal,
            get_neighbors_func=get_neighbors,
            is_free_cell_func=is_free_cell,
        )

        d_result = {
            "seed": seed,
            "path_found": d_found,
            "path_length": len(d_path),
            "path_cost": d_path_cost,
            "visited_nodes": d_visited,
            "runtime_seconds": d_runtime,
        }

        a_result = {
            "seed": seed,
            "path_found": a_found,
            "path_length": len(a_path),
            "path_cost": a_path_cost,
            "visited_nodes": a_visited,
            "runtime_seconds": a_runtime,
        }

        dijkstra_results.append(d_result)
        astar_results.append(a_result)

        print(f"Seed {seed} | Dijkstra: {d_result}")
        print(f"Seed {seed} | A*:       {a_result}")

    dijkstra_average = compute_average_results(dijkstra_results)
    astar_average = compute_average_results(astar_results)

    comparison_data = {
        "dijkstra_results": dijkstra_results,
        "astar_results": astar_results,
        "dijkstra_average": dijkstra_average,
        "astar_average": astar_average,
    }

    print("\nDijkstra average:")
    print(dijkstra_average)

    print("\nA* average:")
    print(astar_average)

    save_results_to_json(
        comparison_data,
        "outputs/logs/dijkstra_astar_multiple_seeds.json"
    )

    plot_average_visited_nodes(
        dijkstra_average,
        astar_average,
        "outputs/figures/dijkstra_astar_average_visited_nodes.png"
    )

    plot_average_runtime(
        dijkstra_average,
        astar_average,
        "outputs/figures/dijkstra_astar_average_runtime.png"
    )


if __name__ == "__main__":
    run_comparison_multiple_seeds()
