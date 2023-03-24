from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    name = "telefonultau"
    allowed_domains = ["telefonultau.eu"]
    start_urls = ["https://telefonultau.eu/"]

    rules = (
        Rule(LinkExtractor(allow="p/telefoane-mobile/"),callback="parse_item"),
        #Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
    )

    def print_rules(self):
        print(self.rules)

    def parse_item(self, response):
        yield {
            "title": response.css(".product-body-title-details h1::text").get(),
            #"price": response.css(".price_color::text").get(),
            #"availability": response.css(".availability::text")[1].get().replace("\n","").replace(" ","")
        }