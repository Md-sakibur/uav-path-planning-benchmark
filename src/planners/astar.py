import heapq
import time


def heuristic(position, goal):
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])


def reconstruct_path(came_from, current):
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path


def run_astar(grid, start, goal, get_neighbors_func, is_free_cell_func):
    start_time = time.perf_counter()

    rows, cols = grid.shape

    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    g_costs = {start: 0}
    came_from = {}
    visited = set()

    while priority_queue:
        current_priority, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            path = reconstruct_path(came_from, current)
            path_cost = g_costs[current]
            visited_count = len(visited)
            runtime = time.perf_counter() - start_time
            return True, path, path_cost, visited_count, runtime

        neighbors = get_neighbors_func(current, rows, cols)

        for neighbor in neighbors:
            if not is_free_cell_func(grid, neighbor):
                continue

            tentative_g_cost = g_costs[current] + 1

            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                came_from[neighbor] = current

                f_cost = tentative_g_cost + heuristic(neighbor, goal)
                heapq.heappush(priority_queue, (f_cost, neighbor))

    runtime = time.perf_counter() - start_time
    return False, [], 0, len(visited), runtime
