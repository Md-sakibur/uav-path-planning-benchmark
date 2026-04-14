import matplotlib.pyplot as plt
import numpy as np


def plot_environment(grid, start, goal, save_path=None):
    display_grid = np.copy(grid)

    plt.figure(figsize=(8, 8))
    plt.imshow(display_grid, cmap="gray_r")

    plt.scatter(start[1], start[0], marker="o", s=100, label="Start")
    plt.scatter(goal[1], goal[0], marker="x", s=100, label="Goal")

    plt.title("UAV Path Planning Environment")
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    plt.show()
