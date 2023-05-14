from urllib.parse import urlencode

import scrapy
from parsel import Selector
import sys, os

from scrapy import Request
from scrapy.loader import ItemLoader

sys.path.append(os.path.join(os.path.abspath('../')))
from models.Product import Product
from Utils import VexioXPaths

API_KEY='0a1ae3c6-9ad0-4ba0-a506-16b17f517275'

def get_proxy_url(url):
    payload={ 'api_key' : API_KEY, 'url' :url}
    proxy_url='https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

class VexioCrawler(scrapy.Spider):
    name = "vexio_crawler"
    #allowed_domains = ["vexio.ro","www.vexio.ro"]

    #start_urls = ["https://www.vexio.ro/smartphone/"]

    def start_requests(self):
        start_url="https://www.vexio.ro/smartphone/"
        yield scrapy.Request(url=get_proxy_url(start_url),callback=self.parse)

    def parse(self, response):
        item_links = []
        item_links = response.xpath(VexioXPaths.VexioXPaths.product_box).getall()
        for item_link in item_links:
            selector = Selector(item_link)
            availability = selector.xpath(
                VexioXPaths.VexioXPaths.product_availability).get().replace("\t", "").replace("\n", "")


            if "nu este in stoc" in availability.casefold():
                continue
            product = Product()
            product['main_site']="vexio.ro"

            title = (selector.xpath(VexioXPaths.VexioXPaths.product_manufacturer).get() + " " +
                     selector.xpath(VexioXPaths.VexioXPaths.product_name).get()).replace("\t", "").replace("\n", "")
            url = selector.xpath(VexioXPaths.VexioXPaths.product_url).get()
            price = selector.xpath(VexioXPaths.VexioXPaths.product_price).get().replace("\t", "").replace("\n", "")



            product['title']=title
            product['price']=price
            product['url']=url
            product['availability']=availability

            yield product

        next_page = response.xpath(VexioXPaths.VexioXPaths.next_page).get()
        if next_page:
            yield response.follow(get_proxy_url(next_page), callback=self.parse)
            #yield response.follow(next_page,callback=self.parse)



