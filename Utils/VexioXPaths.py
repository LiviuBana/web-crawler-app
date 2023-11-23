PRODUCT_BOX = "//div[@id='products-list']//form[starts-with(@id,'product_box')]"
PRODUCT_MANUFACTURER = "//div[@class='clearfix']/div[@class ='manufacturer pull-left']/text()"
PRODUCT_NAME = "//h2[@class='name']/a/@title"
PRODUCT_URL = "//a/@href"
PRODUCT_PRICE = "//div[starts-with(@class,'pull-left')]/strong/text()"
PRODUCT_AVAILABILITY = "//div[starts-with(@class,'availability')]/text()"

NEXT_PAGE = "//li[@class='pagination-next']/a/@href"

IMG = "//div[@class='product-details']//div[@class='item active']//img[@class='img-responsive']/@src"
