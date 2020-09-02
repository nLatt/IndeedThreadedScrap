import scrapy


class RatingsSpider(scrapy.Spider):
    name = 'ratings_spider'
    allowed_domains = ['https://www.indeed.fr/cmp/Lidl/reviews']
    start_urls = ['http://https://www.indeed.fr/cmp/Lidl/reviews/']

    def parse(self, response):
        pass
