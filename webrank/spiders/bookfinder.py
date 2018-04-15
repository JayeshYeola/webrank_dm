import csv

import scrapy
import time


class QuotesSpider(scrapy.Spider):
    name = "bookfinder"

    def start_requests(self):

        dataset = open("./isbns.txt", "r")

        urls = []
        baseurl = 'https://www.bookfinder.com/book/'

        for row in dataset.readlines():
            isbn = row
            urlfinal = baseurl + isbn[0:10]
            print urlfinal
            urls.append(urlfinal)

        for url in urls:
            time.sleep(2)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.attributes'):
            yield {
                'ISBN13': quote.css('div h1::text').extract(),
                'ISBN10':quote.css('div h1 span::text').extract(),
                'Book Name': quote.css('div a strong span::text').extract(),
                'Author': quote.css('div p strong a span::text').extract(),
                'Publisher' : quote.css('p span.describe-isbn::text').extract(),
            }
