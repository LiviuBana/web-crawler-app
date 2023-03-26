import scrapy



class ElectroHomeCrawler(scrapy.Spider):
    name = "electro_home_crawler"
    allowed_domains = ["electrohome.ro"]



    # start_urls=["https://www.electrohome.ro/"]

    start_urls = ["https://www.electrohome.ro/Telefoane-Mobile-Smartphone?page={page}#min_price=493&max_price=9995&category_id=50&page=5&path=14_50&sort=p.sort_order&order=ASC&limit=15&old_route=product%2Fcategory"]

    # rules = (
    #     Rule(LinkExtractor(allow="/Telefoane-Mobile-Smartphone"),callback="parse_items"),
    # )

    def parse(self,response):
        item_links = []
        item_links = response.xpath("//div[@class='item product-layout']//div[@class='name']/a/@href").getall()
        for item_link in item_links:
            yield scrapy.Request(item_link, callback=self.parse_item_dir)

        # next_page=response.xpath

    def parse_item_dir(self,response):
        # product=Product()
        # product["name"]=response.xpath("//div[@class='product-info']//h1[@itemprop='name']/text()").get()
        # product["price"]=response.xpath("//div[@class='product-info']//div[@class='price-new']/span[@class='amount']/text()").get()
        # product["availability"]=response.xpath("//div[@class='product-info']//span[@itemprop='availability']/following-sibling::span[1]/text()").get()
        # response.xpath("//ul[@class='pagination']/li/a[text()='>']/@href").get()
        # yield product
        yield {
            'name': response.xpath("//div[@class='product-info']//h1[@itemprop='name']/text()").get(),
            'price': response.xpath(
                "//div[@class='product-info']//div[@class='price-new']/span[@class='amount']/text()").get(),
            'availability': response.xpath(
                "//div[@class='product-info']//span[@itemprop='availability']/following-sibling::span[1]/text()").get()
        }
