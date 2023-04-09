import scrapy
from parsel import Selector


class RombizCrawler(scrapy.Spider):
    name = "dwyn_crawler"
    allowed_domains = ["dwyn.ro"]



    start_urls = ["https://www.dwyn.ro/telefoane-gsm/"]

    def parse(self, response):
        item_links = []
        item_links = response.xpath("//div[@id='products-list']//form[starts-with(@id,'product_box')]").getall()
        for item_link in item_links:
            selector = Selector(item_link)
            yield {
                'name': selector.xpath("//h5[@class='name margin-bottom-xs']/a/text()").get().replace("\t", "").replace("\n", ""),
                'url': selector.xpath("//h5[@class='name margin-bottom-xs']/a/@href").get(),
                'price': selector.xpath(
                    "//div[starts-with(@class,'new-price')]/strong/text()").get().replace("\t",
                                                                                                           "").replace(
                    "\n", ""),
                'availability': selector.xpath(
                    "//div[starts-with(@class,'availability')]/text()").get().replace("\t","").replace("\n", "")
            }

        next_page = response.xpath("//li[@class='pagination-next']/a/@href").get()
        if next_page:
            yield scrapy.Request(next_page,callback= self.parse)