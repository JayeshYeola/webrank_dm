import scrapy
import time

class IDBSpider(scrapy.Spider):
    name = "powells"

    def start_requests(self):
        f = open("./ISBN13s.txt", "r")

        urls = []
        baseurl = 'http://www.powells.com/book/-'

        for row in f.readlines():
            urlfinal = baseurl+row[:13]
            print urlfinal
            urls.append(urlfinal)

        for url in urls:
            time.sleep(2)
            yield scrapy.Request(url=url, callback=self.parse)

        f.close()

    def parse(self, response):
        for div in response.css('div.middle-line'):
            # for div in div_main.css('div#ProductDetail.ProductDetail'):

                book_name = div.css('div#ProductDetail.ProductDetail div h1.book-title::text').extract()
                author= div.css('div#ProductDetail.ProductDetail div span a::text').extract()
                isbn13= div.css('div#ProductDetail.ProductDetail div p::text').extract()[1]
                isbn10= div.css('div#ProductDetail.ProductDetail div p::text').extract()[3]
                # yield {
                #     'Book Name': div.css('h1.book-title::text').extract(),
                #     'Author': div.css('span a::text').extract(),
                #     'ISBN 13': div.css('p::text').extract()[1],
                #     'ISBN 10': div.css('p::text').extract()[3]
                # }
                i= 0
                # for div1 in div_main.css('div#ProductDetails.ProductDetails'):
                for dl in div.css('div#ProductDetails.ProductDetails dl'):

                    title = dl.css('dt::text').extract()
                    value = dl.css('dd::text').extract()
                    j=0
                    for item in title:
                        if (j==0):
                            yield {
                                'Book Name': book_name,
                                'Author': author,
                                'ISBN 13': isbn13,
                                'ISBN 10': isbn10
                            }
                            j +=1
                        yield {
                            'text': title[i],
                            'value': value[i]
                        }
                        i += 1
                # text= "*******************************   Next Book  ***********************************"
                # yield {
                #     'next': text
                # }

        # i=0
        # for div in response.css('div.result-detail.col-xs-8'):
        #     if(i==0):
        #         yield{
        #             'Book Name':div.css('h2 a span::text').extract(),
        #             'Author':div.css('p strong::text').extract(),
        #             'Publisher':div.css('div p#publisher.small span::text').extract(),
        #             'ISBN 10':div.css('div p.isbn.small span a::text').extract()[0],
        #             'ISBN 11':div.css('div p.isbn.small span a::text').extract()[1]
        #         }
        #         i += 1
