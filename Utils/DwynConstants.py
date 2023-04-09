
class DwynConstants():

    product_box="//div[@id='products-list']//form[starts-with(@id,'product_box')]"
    product_name="//h5[@class='name margin-bottom-xs']/a/text()"
    product_url="//h5[@class='name margin-bottom-xs']/a/@href"
    product_price= "//div[starts-with(@class,'new-price')]/strong/text()"
    product_availability="//div[starts-with(@class,'availability')]/text()"

    next_page="//li[@class='pagination-next']/a/@href"