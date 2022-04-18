import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
commodity = soup.find_all('div', class_="col-lg-4 col-md-6 mb-4")

with open("Parsing.txt", "w") as f:
    for n, i in enumerate(commodity, start=1):
        name = i.find('h4', class_="card-title").text.strip()
        price = i.find('h5').text
        print(f"{n}:  {price} за {name}")
        f.write(f"{n}:  {price} за {name}" + '\n')


