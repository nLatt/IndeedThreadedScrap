import scrapy
from color_print import *
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import pprint

class RatingsSpider(scrapy.Spider):
    name = 'reviews'

    custom_settings = {
        "ITEM_PIPELINES": {
               'indeed.pipelines.RatingsPipeline': 400,
        }
    }

    def __init__(self, urls, filename):
        self.counter = 0
        self.start_urls = ["https://www.indeed.fr/cmp/Lidl/reviews"]
        self.urls = urls
        self.filename = filename


    def parse(self, response):
        for url in range(len(self.urls)):
            joined_url = response.urljoin(self.urls[url])
            yield scrapy.Request(url=joined_url, callback=self.parse_reviews)


    def parse_reviews(self, response):
        print("Inside scraper!")
        for review in response.xpath("//div[@class='cmp-Review'][not(contains(@class, 'is-highlighted'))]"):
            text = [x for x in [x.strip() for x in  review.xpath("descendant::*/span[@class='cmp-ReviewAuthor']/descendant-or-self::*/text()").getall()] if len(x) > 1]
            try:
                review = {
                    "review_title": review.xpath("descendant::*/a[@class='cmp-Review-titleLink']/text()").get(),
                    "review_rating": review.xpath("descendant::*/div[@class='cmp-ReviewRating-text']/text()").get(),
                    "review_author": {
                        "job": text[0],
                        "status": text[1],
                        "location": text[2],
                        "date": text[3],
                        },

                    "review_text": review.xpath("descendant::*/div[@class='cmp-Review-text']/descendant-or-self::*/text()").getall(),
                    "review_pros_cons": {
                        "review_pros": review.xpath("descendant::*/div[@class='cmp-ReviewProsCons-prosText']/span/span/text()").get(),
                        "review_cons": review.xpath("descendant::*/div[@class='cmp-ReviewProsCons-consText']/span/span/text()").get()
                        }
                    }
            except Exception as e:
                prRed(e)

            # Checking if important information is present, if thats not the case it wont be passed into the pipeline
            for key in ["review_text", "review_title", "review_rating"]:
                if review[key] == None:
                    prRed("\nWill be discarded, reason: this dataset was incomplete.\neither 'review_text', 'review_title' or 'review_rating' are None.")
                    break
            else:
                prGreen("\nDataset is clean!")
                self.counter += 1
                prRed(self.counter)
                yield review

# to be called when executing the spider from another script
def crawler(urls, filename):
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(RatingsSpider, urls=urls, filename=filename)
    process.start()
