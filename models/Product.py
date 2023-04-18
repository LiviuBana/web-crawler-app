import scrapy


class Product(scrapy.Item):
    main_site=scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    availability=scrapy.Field()

