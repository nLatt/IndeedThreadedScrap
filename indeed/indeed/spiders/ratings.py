import scrapy


class RatingsSpider(scrapy.Spider):
    name = 'ratings'
    start_urls = ['http://https://www.indeed.fr/cmp/Lidl/reviews/']

    def parse(self, response): # add an argument for the urls that get attributed to this process

        pass
