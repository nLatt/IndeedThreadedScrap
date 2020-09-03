import scrapy
from ..Lib.prcolor import *
import pprint

class RatingsSpider(scrapy.Spider):
    name = 'reviews'
    start_urls = ['https://www.indeed.fr/cmp/Lidl/reviews/']

    custom_settings = {
        "ITEM_PIPELINES": {
               # 'indeed.pipelines.RatingUrlsPipeline': 400,
        }
    }

    def parse(self, response): # add an argument for the urls that get attributed to this process

        pp = pprint.PrettyPrinter(indent=4)

        for review in response.xpath("//div[@class='cmp-Review-container']"):
            text = [x for x in [x.strip() for x in  review.xpath("div/div/span[@class='cmp-ReviewAuthor']/descendant-or-self::*/text()").getall()] if len(x) > 1]
            try:
                review = {
                    "review_rating"
                    "review_title": review.xpath("div/div/a[@class='cmp-Review-titleLink']/text()").get(),

                    "review_author": {
                        "job": text[0],
                        "status": text[1],
                        "location": text[2],
                        "date": text[3],
                        },

                    # "review_text": review.xpath(),
                    # "review pro_con": review.xpath()
                    }
            except Exception as e:
                prRed(e)

            pp.pprint(review)

        pass
