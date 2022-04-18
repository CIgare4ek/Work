import requests
from bs4 import BeautifulSoup
import os


url = "http://quotes.toscrape.com/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
quotes = soup.find_all('span', class_="text")
author = soup.find_all('small', class_="author")
tags = soup.find_all("div", class_="tags")
my_list = list()

with open("Parsing.txt", "w") as f:
    for i in range(0, len(quotes)):
        print(quotes[i].text)
        f.write(quotes[i].text + "\n")
        print("--" + author[i].text)
        tagsforquate = tags[i].find_all("a", class_="tag")
        for tagsforquate in tagsforquate:
            print(tagsforquate.text)
        print("\n")






