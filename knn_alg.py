import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss


def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))


def majority_vote(votes):
    return ss.mode(votes)


def find_nearest_neighbours(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i, p_ in enumerate(points):
        distances[i] = distance(p, p_)
    ind = np.argsort(distances)
    return ind[0:k]


def knn_predict(p, points, classes, k=5):
    ind = find_nearest_neighbours(p, points)
    return majority_vote(classes[ind])[0]


def generate_senthetic_data(n=50):
    temp1 = ss.norm(0, 1).rvs((n, 2))
    temp2 = ss.norm(1, 1).rvs((n, 2))
    points = np.concatenate((temp1, temp2,), axis=0)
    outcomes = np.concatenate((np.repeat(1, n), np.repeat(0, n)))
    # Creating list of the value repeated n times
    return points, outcomes


def make_prediction_grid(predictors, outcomes, limits, h, k=5):
    x_min, x_max, y_min, y_max = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)  # Create a grid with hep of which
    # We can refer to the values like to the coordinates (1,2) or (3,1)
    temp = np.meshgrid(xs, ys)
    prediction_grid = np.zeros(xx.shape, dtype=int)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            p = np.array([x, y])
            prediction_grid[j, i] = knn_predict(p, predictors, outcomes, k)

    return xx, yy, prediction_grid


def plot_prediction_grid(xx, yy, prediction_grid):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap(["hotpink", "lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap(["red", "blue", "green"])
    plt.figure(figsize=(10, 10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap=background_colormap, alpha=0.5)
    plt.scatter(predictors[:, 0], predictors[:, 1], c=outcomes, cmap=observation_colormap, s=50)
    plt.xlabel('Variable 1')
    plt.ylabel('Variable 2')
    plt.xticks(())
    plt.yticks(())
    plt.xlim(np.min(xx), np.max(xx))
    plt.ylim(np.min(yy), np.max(yy))
    plt.show()


predictors, outcomes = generate_senthetic_data()
k = 5
limits = (4, 8, 1.5, 4.5)
h = 0.1
xx, yy, prediction_grip = make_prediction_grid(predictors, outcomes, limits,
                                               h, k)
