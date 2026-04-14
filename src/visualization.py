import matplotlib.pyplot as plt
import numpy as np


def plot_environment(grid, start, goal, path=None, save_path=None):
    display_grid = np.copy(grid)

    plt.figure(figsize=(8, 8))
    plt.imshow(display_grid, cmap="gray_r")

    if path:
        path_rows = [position[0] for position in path]
        path_cols = [position[1] for position in path]
        plt.plot(path_cols, path_rows, linewidth=2, label="Path")

    plt.scatter(start[1], start[0], marker="o", s=100, label="Start")
    plt.scatter(goal[1], goal[0], marker="x", s=100, label="Goal")

    plt.title("UAV Path Planning Environment")
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    plt.show()
