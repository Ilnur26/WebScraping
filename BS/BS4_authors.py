import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, 'html.parser')
with open('bs4authors.csv', 'w', encoding='utf-8') as f:
    for tag in soup.findAll('small', {'class': 'author'}):
        f.write(tag.string)
        f.write('\n')
