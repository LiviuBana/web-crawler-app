import os
import sys

import scrapy
from parsel import Selector

from Utils.PhoneDetailsGetter import PhoneDetailsGetter

sys.path.append(os.path.join(os.path.abspath('../')))
from models.Product import Product
from Utils import DwynXPaths


class DwynCrawler(scrapy.Spider):
    name = "dwyn_crawler"
    allowed_domains = ["dwyn.ro"]

    start_urls = ["https://www.dwyn.ro/telefoane-gsm/"]

    def parse(self, response):
        item_links = []
        item_links = response.xpath(DwynXPaths.PRODUCT_BOX).getall()
        for item_link in item_links:
            selector = Selector(item_link)

            availability = selector.xpath(
                DwynXPaths.PRODUCT_AVAILABILITY).get().replace("\t", "").replace("\n", "")

            if "nu este in stoc" in availability.casefold():
                continue

            product = Product()
            product['main_site'] = "https://www.dwyn.ro/"
            product['logo_url'] = "https://p1.akcdn.net/partnerlogosmall/35559.jpg"

            title = selector.xpath(DwynXPaths.PRODUCT_NAME).get().replace("\t", "").replace("\n", "")
            url = selector.xpath(DwynXPaths.PRODUCT_URL).get()
            price = selector.xpath(DwynXPaths.PRODUCT_PRICE).get().replace("\t", "").replace("\n",
                                                                                                        "").replace(
                "lei", "").strip()

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

        next_page = response.xpath(DwynXPaths.NEXT_PAGE).get()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)
