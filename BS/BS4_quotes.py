import requests
from bs4 import BeautifulSoup


r = requests.get("https://quotes.toscrape.com")
html = r.text
# soup = BeautifulSoup(html, 'html.parser')
soup = BeautifulSoup(html,
                     'lxml'
                     # ,multi_valued_attributes=None
                     )
# print(soup.title.string)
# print(soup.title.parent)
# print(soup.title.parent.name)
with open('bs4quotes.txt', 'w') as f:
    for tag in soup.findAll('span'):
        # print(type(tag))
        # print(tag.name)
        # print(tag.attrs)
        if 'class' in tag.attrs and tag['class'] == ['text']:
            quote = tag.string.strip('“”')
        if tag.small:
            author = tag.small.string
            print(author + ',', quote)
        # f.write(tag.string.strip('“”'))
        # f.write('\n')

        # print(tag.string)
        # print('-------------------------')
# print(soup.span)

# with open("Authors.txt", 'w') as f:
#     for line in html.split("\n"):
#         if '<small class="author" itemprop="author">' in line:
#             line = line.replace('<span>by <small class="author" itemprop="author">', '')
#             line = line.replace('</small>', '').strip()
#             f.write(line)
#             f.write('\n')