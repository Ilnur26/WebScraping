import scrapy
from scrapy import Request

class ScratchImdb(scrapy.Spider):
    name = 'boss'
    start_urls = ['https://www.hugoboss.com/home/']

    def parse(self, response):
        cssSel = 'a[href="https://www.hugoboss.com/men-clothing/"] + div .col-xl-offset-1 a::attr(href)'
        for url in response.css(cssSel).getall():
            yield Request(url, callback=self.parseProducts)


    def parseProducts(self, response):
        print(response.url)
        cssSel = '.product-tile-plp__gallery a::attr("href")'
        for prodUrl in response.css(cssSel).getall():
            # print(prodUrl)
            yield response.follow(prodUrl, callback=self.parseProduct)

        nextPage = response.css('.button.button--pagingbar.pagingbar__next.font--button.button.button--pagingbar.pagingbar__next.font--button::attr("href")').get()
        if nextPage:
            yield Request(nextPage, callback=self.parseProducts)
        # print(NextPage)



    def parseProduct(self, response):
        title = response.css('.pdp-stage__header-title::text').get().strip('\n')
        colors = ', '.join(response.css('.color-selector a::attr("title")').getall())
        picsUrl = response.css('.pdp-images__adaptive-picture source:first-child::attr("srcset")').getall()
        careIns = ', '.join(response.css('.care-info__text::text').getall())
        # print(title)
        # print(colors)
        # print(picsUrl)
        # print(careIns)
        yield {
            'Product Name': title,
            'Colors': colors,
            'Pic Urls': picsUrl,
            'Care Instractions': careIns
        }