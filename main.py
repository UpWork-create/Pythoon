import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter
import re

with open("essay2.1.csv", errors="ignore") as f:
    data = "".join(re.findall("[A-Za-z0-9-,\s]", f.read()))

Capital = []
Proceeds = []
Costs = []
Profit = []

for line in data.split("\n")[1::10]:
    data = line.split()
    Capital.append(data[0])
    Proceeds.append(float(data[1].replace(",", ".")))
    Costs.append(float(data[2].replace(",", ".")))
    Profit.append(float(data[3].replace(",", ".")))

x_indexes = np.arange(len(Capital))
x_values = [i for i in range(0, 100, 10)]
width = 0.25

plt.bar(x_indexes - width, Proceeds, width=width, color="#1ecbe1", label="Proceeds")
plt.bar(x_indexes, Costs, width=width, color="#1ae551", label="Costs")
plt.bar(x_indexes + width, Profit, width=width, color="#64989b", label="Profit")

plt.ylim([-5, 45])
plt.yticks(np.arange(-5, 45, 5))
plt.xticks(ticks=x_indexes, labels=x_values)

plt.legend()
plt.show()
