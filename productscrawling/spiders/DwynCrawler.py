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
        item_links = response.xpath(DwynXPaths.DwynXPaths.product_box).getall()
        for item_link in item_links:
            selector = Selector(item_link)

            availability = selector.xpath(
                DwynXPaths.DwynXPaths.product_availability).get().replace("\t", "").replace("\n", "")

            if "nu este in stoc" in availability.casefold():
                continue

            product = Product()
            product['main_site'] = "https://www.dwyn.ro/"
            product['logo_url'] = "https://p1.akcdn.net/partnerlogosmall/35559.jpg"

            title = selector.xpath(DwynXPaths.DwynXPaths.product_name).get().replace("\t", "").replace("\n", "")
            url = selector.xpath(DwynXPaths.DwynXPaths.product_url).get()
            price = selector.xpath(DwynXPaths.DwynXPaths.product_price).get().replace("\t", "").replace("\n", "")

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

        next_page = response.xpath(DwynXPaths.DwynXPaths.next_page).get()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)
