import heapq
import time


def reconstruct_path(came_from, current):
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path


def run_dijkstra(grid, start, goal, get_neighbors_func, is_free_cell_func):
    start_time = time.perf_counter()

    rows, cols = grid.shape

    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    distances = {start: 0}
    came_from = {}
    visited = set()

    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            path = reconstruct_path(came_from, current)
            path_cost = distances[current]
            visited_count = len(visited)
            runtime = time.perf_counter() - start_time
            return True, path, path_cost, visited_count, runtime

        neighbors = get_neighbors_func(current, rows, cols)

        for neighbor in neighbors:
            if not is_free_cell_func(grid, neighbor):
                continue

            new_distance = current_distance + 1

            if neighbor not in distances or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                came_from[neighbor] = current
                heapq.heappush(priority_queue, (new_distance, neighbor))

    runtime = time.perf_counter() - start_time
    return False, [], 0, len(visited), runtime
