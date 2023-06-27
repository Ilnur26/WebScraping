import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, 'lxml')
tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.findAll('tr')
with open('imdb_quiz.csv', 'w', encoding='utf-8') as f:
    for tr in trs:
        td = tr.find('td', {'class': 'titleColumn'})
        td_rate = tr.find('td', {'class': ['ratingColumn', 'imdbRating']})
        title = td.a.string
        year = td.span.string.strip('()')
        rating = td_rate.strong.string
        f.write(title + ',' + year + ',' + rating)
        f.write('\n')
