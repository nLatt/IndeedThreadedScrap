import scrapy


class LidlRatingsSpider(scrapy.Spider):
    name = 'lidl_ratings'
    allowed_domains = ['https://www.indeed.fr/cmp/Lidl/reviews']
    start_urls = ['https://www.indeed.fr/cmp/Lidl/reviews/']

    def parse(self, response):
        all_links_xpath = response.xpath("//a[@class='icl-Button icl-Button--tertiary icl-Button--lg']/@href").getall()
        # all_links_css = response.css("a.icl-Button::attr(href)").getall()
        print("\n\n\n", all_links_xpath)
        pass
