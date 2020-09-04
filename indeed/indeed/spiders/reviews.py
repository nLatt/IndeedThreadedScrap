import scrapy
from color_print import *
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import pprint

class RatingsSpider(scrapy.Spider):
    name = 'reviews'

    custom_settings = {
        "ITEM_PIPELINES": {
               'indeed.pipelines.RatingUrlsPipeline': 400,
        }
    }

    def __init__(self, url):
        self.start_urls = ["https://www.indeed.fr/cmp/Lidl/reviews" + url]
        prRed(url)


    def parse(self, response): # add an argument for the urls that get attributed to this process

        pp = pprint.PrettyPrinter(indent=4)

        for review in response.xpath("//div[@class='cmp-Review-container']"):
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

            for key in ["review_text", "review_title", "review_rating"]:
                if review[key] == None:
                    prRed("\nWill be discarded, reason: this dataset was incomplete.\neither 'review_text', 'review_title' or 'review_rating' are None.")
                    break
            else:
                prGreen("\nDataset is clean!")
                yield review
            prCyan("lol")
            # continue

        prRed("kek")


if __name__ == "__main__":
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(RatingsSpider, url="?start=1400")
    process.start()
