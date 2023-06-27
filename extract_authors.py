import requests

r = requests.get("https://quotes.toscrape.com")
html = r.text
with open("Authors.txt", 'w') as f:
    for line in html.split("\n"):
        if '<small class="author" itemprop="author">' in line:
            line = line.replace('<span>by <small class="author" itemprop="author">', '')
            line = line.replace('</small>', '').strip()
            f.write(line)
            f.write('\n')
