import json


def summarize_results(found, path, path_cost, visited_count, runtime):
    return {
        "path_found": found,
        "path_length": len(path),
        "path_cost": path_cost,
        "visited_nodes": visited_count,
        "runtime_seconds": runtime,
    }


def save_results_to_json(results, save_path):
    with open(save_path, "w") as file:
        json.dump(results, file, indent=4)
