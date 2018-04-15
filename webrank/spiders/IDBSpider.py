import scrapy
import csv
import time

class IDBSpider(scrapy.Spider):
    name = "isbndb"
    def start_requests(self):
        dataset = open("./data/goodreads.csv", "r")
        bookrow = csv.reader(dataset)
        header = bookrow.next()

        urls = []
        baseurl = 'https://isbndb.com/search/books/'

        for row in bookrow:
            isbn = row[5]
            urlfinal = baseurl+isbn
            print urlfinal
            urls.append(urlfinal)

        for url in urls:
            time.sleep(2)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        i=2
        count = 0
        for dl in response.css('dl'):
            for item in dl.css('dt'):
                print item
                title = item.css('strong::text').extract_first()
                if(title == "Authors:" or title == "Publisher:"):
                    value = dl.css('dt a::text').extract()[count]
                    count += 1
                else:
                    value = dl.css('dt::text').extract()[i]
                i +=2
                yield {
                    'text': title,
                    'value': value,
                }