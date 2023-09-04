import os
import sys

import scrapy
from parsel import Selector

from Utils.PhoneDetailsGetter import PhoneDetailsGetter
from models.Product import Product

sys.path.append(os.path.join(os.path.abspath('../')))
from Utils import RombizXPaths


class RombizCrawler(scrapy.Spider):
    name = "rombiz_crawler"
    allowed_domains = ["rombiz.ro"]

    start_urls = ["https://www.rombiz.ro/telefoane-mobile/"]

    def parse(self, response):
        product_boxes = []
        product_boxes = response.xpath(RombizXPaths.RombizXPaths.product_box).getall()
        for product_box in product_boxes:
            selector = Selector(product_box)

            availability = selector.xpath(RombizXPaths.RombizXPaths.product_availability).get() \
                .replace("\t", "").replace("\n", "")

            if "nu este in stoc" in availability.casefold():
                continue

            product = Product()

            product['main_site'] = "https://www.rombiz.ro/"
            product['logo_url'] = "https://p1.akcdn.net/partnerlogosmall/82915.jpg"
            title = selector.xpath(RombizXPaths.RombizXPaths.product_name).get().replace("\t", "").replace("\n", "")
            url = selector.xpath(RombizXPaths.RombizXPaths.product_url).get()
            price = selector.xpath(RombizXPaths.RombizXPaths.product_price).get() \
                .replace("\t", "").replace("\n", "").replace("lei", "").strip()

            phone_details_getter = PhoneDetailsGetter()
            phone_details = phone_details_getter.get_details(title)

            if phone_details is None:
                continue

            product['producer'] = phone_details[0]
            product['model'] = phone_details[1]
            product['title'] = title
            product['price'] = price
            product['url'] = url
            product['availability'] = availability

            yield product

        next_page = response.xpath(RombizXPaths.RombizXPaths.next_page).get()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)
