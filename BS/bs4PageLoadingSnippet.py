from urllib.request import urlopen, Request
from urllib.parse import urlparse
from bs4 import BeautifulSoup as soup

def checkURL(requested_url):
    if not urlparse(requested_url).scheme:
        requested_url = "https://" + requested_url
    return requested_url


def requestAndParse(requested_url):
    requested_url = checkURL(requested_url)
    try:
        # define headers to be provided for request authentication
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                        'AppleWebKit/537.11 (KHTML, like Gecko) '
                        'Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        request_obj = Request(url=requested_url,headers=headers)
        opened_url = urlopen(request_obj)
        page_html = opened_url.read()
        opened_url.close()
        page_soup = soup(page_html, "html.parser")
        return page_soup, requested_url

    except Exception as e:
        print(e)

# Exmaple:
# page, url = requestAndParse(url)