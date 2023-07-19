import os
import sys

from scrapy.utils.log import configure_logging
from twisted.trial import runner

from productscrawling.spiders.DwynCrawler import DwynCrawler
from productscrawling.spiders.RombizCrawler import RombizCrawler
from productscrawling.spiders.VexioCrawler import VexioCrawler


from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import defer, reactor

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(DwynCrawler)
    yield runner.crawl(VexioCrawler)
    yield runner.crawl(RombizCrawler)
    reactor.stop()

if __name__ == '__main__':
    configure_logging(get_project_settings())
    runner=CrawlerRunner(get_project_settings())
    crawl()
    reactor.run()



