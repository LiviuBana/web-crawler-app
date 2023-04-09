

class VexioConstans():

    product_box="//div[@id='products-list']//form[starts-with(@id,'product_box')]"
    product_manufacturer="//div[@class='clearfix']/div[@class ='manufacturer pull-left']/text()"
    product_name="//h2[@class='name']/a/@title"
    product_url="//a/@href"
    product_price="//div[starts-with(@class,'pull-left')]/strong/text()"
    product_availability="//div[starts-with(@class,'availability')]/text()"

    next_page="//li[@class='pagination-next']/a/@href"
