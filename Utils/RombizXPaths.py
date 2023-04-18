
class RombizXPaths():

    product_box="//form[starts-with(@id,'product_box')]"
    product_name="//h2[@class='h5 name']/a/text()"
    product_url="//h2[@class='h5 name']/a/@href"
    product_price="//div[@class='price clearfix']/div[starts-with(@class,'pull-left')]/strong/text()"
    product_availability="//div[@class='clearfix']/div[starts-with(@class,'availability')]/text()"

    next_page="//li[@class='pagination-next']/a/@href"