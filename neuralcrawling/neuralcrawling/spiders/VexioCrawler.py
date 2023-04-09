import scrapy
from parsel import Selector
import sys,os

sys.path.append(os.path.join(os.path.abspath('../')))
from Utils import VexioConstants


class VexioCrawler(scrapy.Spider):
    name = "vexio_crawler"
    allowed_domains = ["vexio.ro"]

    start_urls = ["https://www.vexio.ro/smartphone/"]

    def parse(self, response):
        item_links = []
        item_links = response.xpath(VexioConstants.VexioConstans.product_box).getall()
        for item_link in item_links:
            selector = Selector(item_link)
            yield {
                'name': (selector.xpath(VexioConstants.VexioConstans.product_manufacturer).get() + " " + selector.xpath(
                    VexioConstants.VexioConstans.product_name).get()).replace("\t", "").replace("\n", ""),
                'url': selector.xpath(VexioConstants.VexioConstans.product_url).get(),
                'price': selector.xpath(VexioConstants.VexioConstans.product_price).get().replace("\t",
                                                                                                           "").replace(
                    "\n", ""),
                'availability': selector.xpath(
                    VexioConstants.VexioConstans.product_availability).get().replace("\t", "").replace("\n", "")
            }

        next_page = response.xpath(VexioConstants.VexioConstans.next_page).get()
        if next_page:
            yield scrapy.Request(next_page,callback= self.parse)
