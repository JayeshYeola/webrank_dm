from scrapy import cmdline
# cmdline.execute("scrapy crawl bookfinder -o ./data/bookfinder2.json".split())
#cmdline.execute("scrapy crawl abebooks -o ./data/abebooks2.json".split())
cmdline.execute("scrapy crawl isbndb -o ./data/isbndb2.json".split())
# cmdline.execute("scrapy crawl powells -o ./data/powells.json".split())