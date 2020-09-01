import scrapy
import re
from scrapy.linkextractors import LinkExtractor


class LidlRatingsSpider(scrapy.Spider):
    name = 'lidl_ratings'
    # allowed_domains = ['https://www.indeed.fr']
    start_urls = ['https://www.indeed.fr/cmp/Lidl/reviews']
    all_links = ["?start=00"]

    def parse(self, response):
        try:
            all_links_xpath = response.xpath("//a[@class='icl-Button icl-Button--tertiary icl-Button--lg']/@href").getall()
            regexed_links = [re.search(r"[?](.*)", x).group() for x in all_links_xpath if re.search(r"[?](.*)", x) != None]
            try:
                [self.all_links.append(x) for x in regexed_links if x not in self.all_links]
            except Exception as e:
                print(e)

            link_to_go_to = self.start_urls[0] + self.all_links[-1]

            # Go to the last rating page that is linked on the current page
            url = response.urljoin(self.all_links[-1])
            yield scrapy.Request(url, callback=self.parse)

            print(self.all_links)
        except Exception as e:
            print(e)
        # all_links_css = response.css("a.icl-Button::attr(href)").getall()
        pass
