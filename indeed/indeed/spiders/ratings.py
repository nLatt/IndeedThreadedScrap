import scrapy
from ..Lib.prcolor import *
import pprint

class RatingsSpider(scrapy.Spider):
    name = 'ratings'
    start_urls = ['https://www.indeed.fr/cmp/Lidl/reviews/']

    custom_settings = {
        "ITEM_PIPELINES": {
               # 'indeed.pipelines.RatingUrlsPipeline': 400,
        }
    }

    def parse(self, response): # add an argument for the urls that get attributed to this process

        pp = pprint.PrettyPrinter(indent=4)

        for rating in response.xpath("//div[@class='cmp-Review-container']"):
            descendant_text = rating.xpath("div/div/span[@class='cmp-ReviewAuthor']/descendant::*/text()").getall()
            current_text = [x for x in [x.strip() for x in  rating.xpath("div/div/span[@class='cmp-ReviewAuthor']/text()").getall()] if len(x) > 1]
            rating = {
                "rating_title": rating.xpath("div/div/a[@class='cmp-Review-titleLink']/text()").get(),

                "rating_author": {
                    "job": descendant_text[0],
                    "location": descendant_text[1],
                    "status": current_text[0],
                    "date": current_text[1],
                    },
                # "rating_text": rating.xpath(),
                # "rating pro_con": rating.xpath()
                }

            pp.pprint(rating)

        pass
