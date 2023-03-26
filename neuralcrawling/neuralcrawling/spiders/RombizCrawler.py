import scrapy
from parsel import Selector


class RombizCrawler(scrapy.Spider):
    name = "rombiz_crawler"
    allowed_domains = ["rombiz.ro"]

    # start_urls=["https://www.electrohome.ro/"]

    start_urls = ["https://www.rombiz.ro/telefoane-mobile/"]

    # rules = (
    #     Rule(LinkExtractor(allow="/Telefoane-Mobile-Smartphone"),callback="parse_items"),
    # )

    def parse(self, response):
        item_links = []
        item_links = response.xpath("//form[starts-with(@id,'product_box')]").getall()
        for item_link in item_links:
            selector = Selector(item_link)
            yield {
                'name': selector.xpath("//h2[@class='h5 name']/a/text()").get().replace("\t", "").replace("\n", ""),
                'url': selector.xpath("//h2[@class='h5 name']/a/@href").get(),
                'price': selector.xpath(
                    "//div[@class='price clearfix']/div[starts-with(@class,'pull-left')]/strong/text()").get().replace("\t",
                                                                                                           "").replace(
                    "\n", ""),
                'availability': selector.xpath(
                    "//div[@class='clearfix']/div[starts-with(@class,'availability')]/text()").get().replace("\t",
                                                                                                                "").replace(
                    "\n", "")
            }

        next_page = response.xpath("//li[@class='pagination-next']/a/@href").get()
        if next_page:
            yield scrapy.Request(next_page,callback= self.parse)
