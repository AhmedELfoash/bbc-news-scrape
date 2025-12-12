import requests
from bs4 import BeautifulSoup
import pandas as pd


rss_url = "https://feeds.bbci.co.uk/news/rss.xml"
response = requests.get(rss_url)
if response.status_code != 200:
    print("Error loading RSS feed")
    exit()

soup = BeautifulSoup(response.content, "xml")

news_list = []

print("---------- Latest 10 BBC News Articles ----------\n")

for idx, item in enumerate(soup.find_all("item")[:10], start=1):
    title = item.title.text if item.title else "No Title"
    link = item.link.text if item.link else "No Link"
    summary = item.description.text if item.description else "No Summary"
    date = item.pubDate.text if item.pubDate else "No Date"

    news_list.append({
        "Title": title,
        "Link": link,
        "Summary": summary,
        "Date": date
    })

    print(f"Article {idx}:")
    print(f"Title   : {title}")
    print(f"Link    : {link}")
    print(f"Summary : {summary}")
    print(f"Date    : {date}")
    print("-" * 70)


df = pd.DataFrame(news_list)
df.to_csv("bbc_news_scraped.csv", index=False, encoding='utf-8-sig')

print("\nNews has been collected and saved to bbc_news_scraped.csv")
