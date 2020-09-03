import scrapy
import re
from ..Lib.prcolor import *

class RatingUrlsSpider(scrapy.Spider):
    name = 'review_urls'
    # start_urls = ["https://www.indeed.fr/cmp/Lidl/reviews?fcountry=ALL"]
    start_urls = ['https://www.indeed.fr/cmp/Lidl/reviews']
    already_scraped_links = []

    custom_settings = {
        "ITEM_PIPELINES": {
               'indeed.pipelines.RatingUrlsPipeline': 400,
        }
    }

    def parse(self, response):
        try:
            all_links_xpath = response.xpath("//a[@class='icl-Button icl-Button--tertiary icl-Button--lg']/@href").getall()
            regexed_links = [re.search(r"[?](.*)", x).group() for x in all_links_xpath if re.search(r"[?](.*)", x) != None]
            links = [x for x in regexed_links if x not in self.already_scraped_links]

            # Go to the last rating page that is linked on the current page
            if links == []:
                prRed("Scraped all URLs!")
                return

            links.pop() # removes the last element of the list, its the same as links[0]
            url = response.urljoin(links[-1])
            yield scrapy.Request(url, callback=self.parse)

        except Exception as e:
            prRed(e)

        for link in links:
            if link not in self.already_scraped_links:
                yield {
                    "link": link
                }
                self.already_scraped_links.append(link)
