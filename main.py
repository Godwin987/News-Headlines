from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import time
import csv

options = Options()
options.add_argument("headless")
driver = webdriver.Edge(options=options)
driver.get("https://www.channelstv.com/")
page_source = driver.page_source
# print(page_source)

soup = BeautifulSoup(page_source, "html.parser")

headlines = soup.find(name="div", class_="latest_stories")
post_title = headlines.find_all(name="h3", class_="post-title")

news = {}
links = {}
for post in post_title:
    title = post.get_text()
    link = post.find_next(name="a")
    news['Headlines'] = title
    links['Links'] = link.attrs["href"]
print(news)
print(links)
# with open('news.csv', 'w', newline='') as news:
#     fieldnames = ['Headlines', 'Links']
#     writer = csv.DictWriter(news, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'Headlines': 'Baked', 'Links': 'Beans'})

# print(post_title)
# for a in headlines:
#     print()
# element = driver.find_elements(by=By.CSS_SELECTOR, value=".latest_stories .post-title")
#
# print(element)

