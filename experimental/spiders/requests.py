# -*- coding: utf-8 -*-
from os.path import join, dirname
from scrapy import Spider
from scrapy.http import Request
import experimental


class RequestsSpider(Spider):
    name = "requests"

    def _requests(self):
        filename = join(dirname(experimental.__file__),
                        self.settings.get('SEEDS', ))
        for line in open(filename):
            try:
                url = line.strip()
                yield url
            except Exception as e:
                self.logger.error('Problem link %s [%s]' % (line, str(e)))

    @classmethod
    def from_crawler(cls, crawler):
        spider = super(RequestsSpider, cls).from_crawler(crawler)
        spider.settings = crawler.settings
        spider.g = spider._requests()
        spider.start_urls = [
            next(spider.g)
        ]
        return spider

    def parse(self, response):
        for x in range(10):
            yield Request(
                url=next(self.g)
            )

        yield {
            'url': response.url
        }
