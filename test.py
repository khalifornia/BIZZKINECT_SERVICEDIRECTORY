import scrapy
from scrapy.crawler import CrawlerProcess

# class QuotesSpider(scrapy.Spider):
#     name = "quotes"

#     def start_requests(self):
#         urls = [
#             'http://quotes.toscrape.com/page/1/',
#             'http://quotes.toscrape.com/page/2/',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = 'quotes-%s.html' % page
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log('Saved file %s' % filename)

# process = CrawlerProcess({
#     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
# })

# process.crawl(QuotesSpider)
# process.start() # the script will block here until the crawling is finished

class ScrapeSourceRecord():

    def __init__(self, source, meta_info):
        self.source = source
        self.meta_info = meta_info


    def run_scraper(self):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        
        if self.source == 'yellowpages':

            process.crawl(YellowPagesSpider)
            process.start()

class YellowPagesSpider(scrapy.Spider):
    name = "yellow_pages"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

x = ScrapeSourceRecord('yellowpages', {"search_terms": "painter"})
x.run_scraper()



class ParentClass():
    def add_numbers(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x-y

class ChildClass(ParentClass):
    def add_numbers(self, numbers):

        return sum(x for x in numbers)

x = ChildClass([1, 2, 3])
x.subtract()

x = ParentClass()
