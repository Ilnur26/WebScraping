import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'
res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = res.text
print('status_code1:', res.status_code)
soup = BeautifulSoup(html, 'html.parser')
# soup = BeautifulSoup(html, 'lxml')
tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.findAll('tr', limit=2)
for tr in trs:
    td = tr.find('td', {'class': 'titleColumn'})
    # print(td.a.string, td.span.string)
    movieId = td.a['href']
    movieUrl = f'https://www.imdb.com/{movieId}'
    res2 = requests.get(movieUrl, headers={'User-Agent': 'Mozilla/5.0'})
    print('status_code2:', res2.status_code)
    html = res2.text
    soup2 = BeautifulSoup(html, 'html.parser')
    # print(html)
    # print('----------------------------------------')
    info = soup2.find('div', {'class': ['sc-52d569c6-0', 'kNzJA-D']})
    duration = info.find('li', {'class': 'ipc-inline-list__item'})
    print(info.h1.span.string, duration.string)
    # info = soup2.find('div', {'class': 'subtext'})
    # print(info.time.string.strip())
    # a = info.findAll('a')
    # print(td.a.string)
    # print(td.span.string)
    # print(a[0].string.strip())
    # print(a[1].string.strip())


# print(info)

# sc-52d569c6-0 kNzJA-D
# sc-52d569c6-0 kNzJA-D