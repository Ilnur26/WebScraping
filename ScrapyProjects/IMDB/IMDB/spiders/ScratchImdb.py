import scrapy

class ScratchImdb(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/']
    # HEADERS = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    #     "Accept-Language": "en-US,en;q=0.5",
    #     "Accept-Encoding": "gzip, deflate",
    #     "Connection": "keep-alive",
    #     "Upgrade-Insecure-Requests": "1",
    #     "Sec-Fetch-Dest": "document",
    #     "Sec-Fetch-Mode": "navigate",
    #     "Sec-Fetch-Site": "none",
    #     "Sec-Fetch-User": "?1",
    #     "Cache-Control": "max-age=0"
    # }

    def parse(self, response):
        for tag in response.css('div a.ipc-title-link-wrapper'):
            # href = tag.css('a::attr(href)').get()
            a = tag.css('a::attr(href)').get()
            movie = tag.css('h3::text').get()
            # year = tag.css('span.sc-14dd939d-6.kHVqMR.cli-title-metadata-item:first-child::text').get()
            url = 'https://www.imdb.com/' + a
            if '.' in movie:
                place = movie.split('.', 1)[0]
                name = movie.split('.', 1)[1]
            else:
                place, name = None, None

            dic = {'movieName': name,
                   'place': place
                   # , 'year': year
                   }

            yield response.follow(url, callback=self.parseInfo, meta=dic, dont_filter=True)

            # break

            # yield {
            #     # 'tag': tag
            #     'place': place,
            #     'name': name,
            #     'a': a
            #     # 'href': href
            # }
        # for h3 in response.css('li a.ipc-title-link-wrapper h3.ipc-title__text'):
        #     quote = div.css('.text::text').get()
        #     author = div.css('.author::text').get()
        #     tags = div.css('.tag::text').getall()
        #     yield {
        #         'quote': quote.replace('“', '').replace('”', ''),
        #         'author': author,
        #         'tags': tags
        #     }


    def parseInfo(self, response):
        # print(response.url)
        duration = response.css('.ipc-inline-list.ipc-inline-list--show-dividers.sc-afe43def-4.kdXikI.baseAlt li:last-child::text').get()
        genre = response.css('div[data-testid="genres"] div a span::text').getall()
        director = response.css('span:contains("Director") + div ul li a::text').get()
        directorUrl = response.css('span:contains("Director") + div ul li a::attr(href)').get()
        name = response.meta['movieName']
        place = response.meta['place']
        # year = response.meta['year']
        yield {
            'NN': place,
            'MovieName': name,
            'Duration': duration,
            'Genre': genre,
            'Director': director
            # ,
            # 'Year': year
        }
        top4Movies = response.css('.ipc-primary-image-list-card__content-top a::text').getall()
        # print('\n\n\n\n')
        # print(txt)
        # print('\n\n\n\n')
        # print(genre)
