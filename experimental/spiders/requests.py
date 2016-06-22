# -*- coding: utf-8 -*-
from os.path import join, dirname
from scrapy import Spider
import experimental


class RequestsSpider(Spider):
    name = "requests"

    def start_requests(self):
        filename = join(dirname(experimental.__file__),
                        self.settings.get('SEEDS', ))
        reqs = []
        for line in open(filename):
            try:
                url = line.strip()
                reqs.append(self.make_requests_from_url(url))
            except Exception as e:
                self.logger.error('Problem link %s [%s]' % (line, str(e)))
        return reqs

    def parse(self, response):
        return {
            'url': response.url
        }
