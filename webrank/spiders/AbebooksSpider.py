import scrapy
import time

class IDBSpider(scrapy.Spider):
    name = "abebooks"

    def start_requests(self):
        f = open("./isbns.txt", "r")

        urls = []
        baseurl = 'https://www.abebooks.com/servlet/SearchResults?sts=t&cm_sp=SearchF-_-home-_-Results&an=&tn=&kn=&isbn='

        for row in f.readlines():
            urlfinal = baseurl+row
            print urlfinal
            urls.append(urlfinal)

        for url in urls:
            time.sleep(2)
            yield scrapy.Request(url=url, callback=self.parse)

        f.close()

    def parse(self, response):
        i=0
        for div in response.css('div.result-detail.col-xs-8'):
            if(i==0):
                yield{
                    'Book Name':div.css('h2 a span::text').extract(),
                    'Author':div.css('p strong::text').extract(),
                    'Publisher':div.css('div p#publisher.small span::text').extract(),
                    'ISBN 10':div.css('div p.isbn.small span a::text').extract()[0],
                    'ISBN 11':div.css('div p.isbn.small span a::text').extract()[1]
                }
                i += 1
