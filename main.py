from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
options.add_argument("headless")
driver = webdriver.Edge(options=options)
driver.get("https://www.channelstv.com/")
page_source = driver.page_source
# print(page_source)

soup = BeautifulSoup(page_source, "html.parser")

headlines = soup.find(name="div", class_="latest_stories")
post_title = headlines.find_all(name="h3", class_="post-title")
for post in post_title:
    print(post.get_text())
# print(post_title)
# for a in headlines:
#     print()
# element = driver.find_elements(by=By.CSS_SELECTOR, value=".latest_stories .post-title")
#
# print(element)

