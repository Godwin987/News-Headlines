from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import csv

"""set the browser in headless mode"""
options = Options()
options.add_argument("headless")

driver = webdriver.Edge(options=options)
driver.get("https://www.channelstv.com/")
page_source = driver.page_source

"""create the soup object"""
soup = BeautifulSoup(page_source, "html.parser")

"""Find all the contents needed in each tag"""
headlines = soup.find(name="div", class_="latest_stories")
post_title = headlines.find_all(name="h3", class_="post-title")
post_time = headlines.find_all(name="span")

"""create empty list for all contents"""
topic = []
links = []
time_ = []

for post in post_time:
    _time = post.text
    time_.append(_time)

for post in post_title:
    title = post.get_text().strip()
    link = post.find_next(name="a")
    topic.append(title)
    links.append(link.attrs['href'])

"""concatenate each list into a list of tuples"""
data = list(zip(topic, links, time_))

"""create the csv file"""
with open('news.csv', mode='w', newline='') as news:
    writer = csv.writer(news)
    writer.writerow(['Topic', 'Link', 'Time'])
    writer.writerows(data)
