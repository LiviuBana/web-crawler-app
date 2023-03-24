
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class ElectroHomeCrawler(scrapy.Spider):
    name="electro_home_crawler"
    allowed_domains=["electrohome.ro"]

    #start_urls=["https://www.electrohome.ro/"]

    start_urls=["https://www.electrohome.ro/Telefoane-Mobile-Smartphone"]
    # rules = (
    #     Rule(LinkExtractor(allow="/Telefoane-Mobile-Smartphone?page={page}"),callback="parse_items"),
    # )

    def parse_items(self,response):
        item_links=[]
        item_links=response.xpath("//div[@class='item product-layout']//div[@class='name']/a/@href").getall()
        for item_link in item_links:
            yield scrapy.Request(item_link,callback=self.parse_item_dir)

        #next_page=response.xpath


    def parse_item_dir(self,response):
        # product=models.Product.Product()
        # product["name"]=response.xpath("//div[@class='product-info']//h1[@itemprop='name']/text()").get()
        # product["price"]=response.xpath("//div[@class='product-info']//div[@class='price-new']/span[@class='amount']/text()").get()
        # product["availability"]=response.xpath("//div[@class='product-info']//span[@itemprop='availability']/following-sibling::span[1]/text()").get()
        #response.xpath("//ul[@class='pagination']/li/a[text()='>']/@href").get()
        # yield product
        return 0

