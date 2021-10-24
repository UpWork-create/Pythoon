import csv
from random import randint
from time import sleep
from itertools import count

titles = ["Indexes", "Chance 6/8", "Change 5/6"]
chance1 = 1000
chance2 = 1000
counter = count()

with open("real-time_data.csv", "w") as csv_f:
    writer = csv.DictWriter(csv_f, fieldnames=titles)
    writer.writeheader()

while True:
    with open("real-time_data.csv", "a") as csv_f:
        writer = csv.DictWriter(csv_f, fieldnames=titles)

        data = [next(counter) + 1, randint(-6, 8), randint(-5, 6)]
        info = {titles[0]: data[0], titles[1]: chance1 + data[1],
                titles[2]: chance2 + data[2]}

        chance1 += data[1]
        chance2 += data[2]

        print(info)
        writer.writerow(info)
    sleep(2)
