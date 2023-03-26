# This is a sample Python script.
from scrapy.crawler import CrawlerProcess


from neuralcrawling.neuralcrawling.spiders.ElectroHomeCrawler import ElectroHomeCrawler
from neuralcrawling.neuralcrawling.spiders.RombizCrawler import RombizCrawler
from neuralcrawling.neuralcrawling.spiders.crawling_spider import CrawlingSpider

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process = CrawlerProcess(settings={
        "FEEDS": {
            "items.json": {"format": "json"},
        },
    })
    process.crawl(RombizCrawler)
    process.start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
