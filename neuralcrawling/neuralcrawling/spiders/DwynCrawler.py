import os
import sys

import scrapy
from parsel import Selector

sys.path.append(os.path.join(os.path.abspath('../')))
from Utils import DwynConstants


class DwynCrawler(scrapy.Spider):
    name = "dwyn_crawler"
    allowed_domains = ["dwyn.ro"]



    start_urls = ["https://www.dwyn.ro/telefoane-gsm/"]

    def parse(self, response):
        item_links = []
        item_links = response.xpath(DwynConstants.DwynConstants.product_box).getall()
        for item_link in item_links:
            selector = Selector(item_link)
            yield {
                'name': selector.xpath(DwynConstants.DwynConstants.product_name).get().replace("\t", "").replace("\n", ""),
                'url': selector.xpath(DwynConstants.DwynConstants.product_url).get(),
                'price': selector.xpath(
                    DwynConstants.DwynConstants.product_price).get().replace("\t",
                                                                                                           "").replace(
                    "\n", ""),
                'availability': selector.xpath(
                    DwynConstants.DwynConstants.product_availability).get().replace("\t","").replace("\n", "")
            }

        next_page = response.xpath(DwynConstants.DwynConstants.next_page).get()
        if next_page:
            yield scrapy.Request(next_page,callback= self.parse)