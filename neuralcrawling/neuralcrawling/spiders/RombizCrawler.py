import os
import sys

import scrapy
from parsel import Selector
sys.path.append(os.path.join(os.path.abspath('../')))
from Utils import RombizConstants


class RombizCrawler(scrapy.Spider):
    name = "rombiz_crawler"
    allowed_domains = ["rombiz.ro"]

    start_urls = ["https://www.rombiz.ro/telefoane-mobile/"]

    def parse(self, response):
        item_links = []
        item_links = response.xpath(RombizConstants.RombizConstans.product_box).getall()
        for item_link in item_links:
            selector = Selector(item_link)
            yield {
                'name': selector.xpath(RombizConstants.RombizConstans.product_name).get().replace("\t", "").replace("\n", ""),
                'url': selector.xpath(RombizConstants.RombizConstans.product_url).get(),
                'price': selector.xpath(
                    RombizConstants.RombizConstans.product_price).get().replace("\t",
                                                                                                           "").replace(
                    "\n", ""),
                'availability': selector.xpath(
                    RombizConstants.RombizConstans.product_availability).get().replace("\t",
                                                                                                                "").replace(
                    "\n", "")
            }

        next_page = response.xpath(RombizConstants.RombizConstans.next_page).get()
        if next_page:
            yield scrapy.Request(next_page,callback= self.parse)
