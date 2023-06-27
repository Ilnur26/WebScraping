import scrapy

class ScratchQuotes(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        for div in response.css('.quote'):
             quote = div.css('.text::text').get()
             author = div.css('.author::text').get()
             yield {
                 'quote': quote.replace('“', '').replace('”', ''),
                 'author': author
             }

        if response.css('li.next').get():
            print('\n\n\n\n NEXT button available')
        else:
            print('\n\n\n\n LAST page')