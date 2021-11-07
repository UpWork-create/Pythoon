import re
from time import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt


def scrape_url():
    df = pd.read_csv("fludda/whisky.csv")
    return df["Link"]


def append_list(url):
    try:
        source = requests.get(url, timeout=1).text
        soup = BeautifulSoup(source, "lxml")
        alco_procent = soup.find("p", class_="product-info-size-abv").find_all("span")
        for item in alco_procent:
            if item.text.count("%") == 1:
                alco_procent = item.text.replace("%", "").replace(",", ".")
                break
        clear_procent = re.search(r"([0-9A-Za-z,/.]+)", alco_procent).group(0)
        print(clear_procent)
        return float(clear_procent)
    except:
        pass


def write_to_csv(list_of_values, path):
    pd_list = [[i + 1, list_of_values[i]] for i in range(len(list_of_values))]
    alcohol = pd.DataFrame(pd_list, columns=["Index", "Alcohol in %"])
    alcohol.set_index(alcohol["Index"], inplace=True, drop=True)
    alcohol.to_csv(path)


def drawing_graph(list_of_values):
    plt.hist(list_of_values, edgecolor="white")
    plt.title("Whisky alcohol statistics")
    plt.xlabel("Alcohol in %")
    plt.ylabel("Numbers of whiskys")
    plt.savefig("whisky.png")


def main():
    x1 = time()
    started_urls = scrape_url()
    list_of_alcohol: list[float] = []
    for num, url in enumerate(started_urls):
        print(f"{num}) ", end="")
        value = append_list(url)
        try:
            if value is not None:
                list_of_alcohol.append(value)
        except:
            print("RAISED ERROR", end="")
    x2 = time()
    write_to_csv(list_of_alcohol, "w.csv")
    drawing_graph(list_of_alcohol)
    print(f"Elapsed time:{round(x2 - x1, 3)}")


if __name__ == "__main__":
    main()
