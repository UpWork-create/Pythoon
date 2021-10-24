import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex="all", sharey="all")


def animate(i):
    data = pd.read_csv("real-time_data.csv")
    indexes = data["Indexes"]
    x = data["Chance 6/8"]
    y = data["Change 5/6"]

    ax1.cla()
    ax2.cla()

    ax2.set_xlabel("Ticks")

    ax1.plot(indexes, x, label="Chance 6/8", color="#139921", linewidth=2)
    ax2.plot(indexes, y, label="Chance 5/6", color="#a12190", linewidth=2)

    ax1.legend(loc="upper left")
    ax2.legend(loc="upper left")


ani = FuncAnimation(plt.gcf(), animate, interval=2000)
plt.show()
