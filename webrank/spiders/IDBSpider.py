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
        i=0
        for url in urls:
            time.sleep(2)
            yield scrapy.Request(url=url, callback=self.parse)
            # if(i==0):
            #     time.sleep(2)
            #     yield scrapy.Request(url=url, callback=self.parse)
            #     i+=1

    def parse(self, response):
        # i=2
        # count = 0
        website = "https://isbndb.com"
        for div in response.css('div.col-md-6.col-xs-6'):

            yield{
                'WebSite': website,
                'Book Name':div.css('h2 a::text').extract(),
                'Author':div.css('dl dt a::text').extract()[0],
                'ISBN 10': div.css('dl dt::text').extract()[6],
                'ISBN 13': div.css('dl dt::text').extract()[8],
                'Edition': div.css('dl dt::text').extract()[10],
                'Publisher':div.css('dl dt a::text').extract()[1],
                'Publishing year': div.css('dl dt::text').extract()[14],
                'Binding': div.css('dl dt::text').extract()[16],
            }


        # for dl in response.css('dl'):
        #     for item in dl.css('dt'):
        #         print item
        #         title = item.css('strong::text').extract_first()
        #         if(title == "Authors:" or title == "Publisher:"):
        #             value = dl.css('dt a::text').extract()[count]
        #             count += 1
        #         else:
        #             value = dl.css('dt::text').extract()[i]
        #         i +=2
        #         yield {
        #             'text': title,
        #             'value': value,
        #         }