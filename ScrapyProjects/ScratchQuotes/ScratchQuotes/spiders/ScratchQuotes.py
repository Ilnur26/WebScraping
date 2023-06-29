import scrapy

class ScratchQuotes(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        for div in response.css('.quote'):
             quote = div.css('.text::text').get()
             author = div.css('.author::text').get()
             tags = div.css('.tag::text').getall()
             yield {
                 'quote': quote.replace('“', '').replace('”', ''),
                 'author': author,
                 'tags': tags
             }

        nextPageUrl = response.css('li.next a::attr(href)').get()
        print(nextPageUrl)

        # if response.css('li.next').get():
        if nextPageUrl:
            yield response.follow(nextPageUrl, callback=self.parse)
            # print('\n\n\n\n NEXT button available')
        else:
            print('\n\n\n\n LAST page')

# nextPageUrl -> /page/2


# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
