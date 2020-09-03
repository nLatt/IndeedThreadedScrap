import scrapy
from ..Lib.prcolor import *

class RatingsSpider(scrapy.Spider):
    name = 'ratings'
    start_urls = ['https://www.indeed.fr/cmp/Lidl/reviews/']

    custom_settings = {
        "ITEM_PIPELINES": {
               # 'indeed.pipelines.RatingUrlsPipeline': 400,
        }
    }

    def parse(self, response): # add an argument for the urls that get attributed to this process
        # print(response.xpath("//div[@class='cmp-Review-container']/@data-tn-entityid").getall())

        for rating in response.xpath("//div[@class='cmp-Review-container']"):
            rating = {
                # "rating": rating.xpath(),
                "rating_content": {
                    "rating_title": rating.xpath("div/div/a[@class='cmp-Review-titleLink']/text()").get(),
                    "rating_author": rating.xpath("div/span[@class='cmp-ReviewAuthor']/text()").getall(),
                    # "rating_text": rating.xpath(),
                    # "rating pro_con": rating.xpath()
                }
            }
            # prRed(rating.xpath("div[@class='cmp-Review-content']/descendant::*/text()").getall())
            prRed(rating)
            # prRed(rating)
            # yield {
            #     "tree": rating.xpath("").get()
            #     }

        pass
