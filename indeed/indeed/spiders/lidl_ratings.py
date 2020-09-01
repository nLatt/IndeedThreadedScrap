import scrapy
import re


class LidlRatingsSpider(scrapy.Spider):
    name = 'lidl_ratings'
    allowed_domains = ['https://www.indeed.fr/cmp/Lidl/reviews']
    start_urls = ['https://www.indeed.fr/cmp/Lidl/reviews']
    all_links = []

    def parse(self, response):
        try:
            all_links_xpath = response.xpath("//a[@class='icl-Button icl-Button--tertiary icl-Button--lg']/@href").getall()
            [self.all_links.append(re.search(r"[?](.*)", x).group()) for x in all_links_xpath]
            self.all_links.pop()
            print("\n\n\n", self.all_links)
            link_to_go_to = self.start_urls[0] + self.all_links[-1]
            print(link_to_go_to)
            # scrapy.Request(link_to_go_to, callback=self.parse(response))
        except Exception as e:
            print(e)
        # all_links_css = response.css("a.icl-Button::attr(href)").getall()
        pass
