import requests

with open('quotes.csv', 'a', encoding='utf-8') as f:
    for i in range(1, 11):
        print('Page: ', i)
        url = f'https://quotes.toscrape.com/page/{i}/'
        r = requests.get(url)
        html = r.text
        author = ''
        quote = ''
        for line in html.split('\n'):
            if '<span class="text" itemprop="text">' in line:
                quote = line.replace('<span class="text" itemprop="text">“', '') \
                            .replace('”</span>', '') \
                            .strip()
            if '<small class="author" itemprop="author">' in line:
                author = line.replace('<span>by <small class="author" itemprop="author">', '') \
                             .replace('</small>', '') \
                             .strip()
                
                f.write(author + ', ' + quote)
                f.write('\n')
