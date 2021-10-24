import csv
import requests
from bs4 import BeautifulSoup

source = requests.get("https://coreyms.com").text
soup = BeautifulSoup(source, "lxml")
csv_file = open("cms_scrape.csv", "w")
csv_writer = csv.DictWriter(csv_file, fieldnames=["Headline", "Summary", "Video Link"])
csv_writer.writeheader()

for article in soup.find_all("article"):
    headline = article.h2.a.text
    summary = article.find("div", class_="entry-content").p.text

    print(headline)
    print(summary)

    try:
        vid_src = article.find("iframe", class_="youtube-player")["src"]
        vid_id = vid_src.split("/")[4].split("?")[0]
        yt_link = f"https://youtube.com/watch?v={vid_id}"
    except:
        yt_link = None
    print(yt_link)
    print()

    csv_writer.writerow({"Headline": headline, "Summary": summary, "Video Link": yt_link})

csv_file.close()
