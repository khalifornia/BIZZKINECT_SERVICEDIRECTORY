# -*- coding: utf-8 -*-
import scrapy


class YpDentistsSpiderSpider(scrapy.Spider):


    name = 'yp_auto_spider'
    # allowed_domains = ['yp.com']
    def __init__(self, page_id, *args, **kwargs):
        super(YpDentistsSpiderSpider, self).__init__(*args, **kwargs)
        self.page_id = page_id


    def start_requests(self):
        url = 'https://www.yellowpages.com/search?search_terms=Dentist&geo_location_terms=Phoenix%2C+AZ&page=' + str(self.page_id)
        yield scrapy.Request(url=url, callback=self.parse_results)

    def parse_results(self, response):
        url_list = []
        for dentist in response.css('div.search-results div.result'):
            url_list.append("https://www.yellowpages.com" + dentist.xpath('.//a[@class="business-name"]/@href').extract_first())
        for url in url_list:

            yield scrapy.Request(url=url, callback=self.parse_listing, meta={'url': url})

            # yield {
            #     'business' : dentist.xpath('.//span[@itemprop="name"]/text()').extract_first(),
            #     'street-address': dentist.xpath('.//span[@itemprop="streetAddress"]/text()').extract_first(),
            #     'phone': dentist.xpath('.//div[@itemprop="telephone"]/text()').extract_first(),
            #     'url': url,
            # }
    def parse_listing(self, response):
        listing_url = response.meta.get('url')

        yield {
            'yp listing url' : listing_url,
            'category' : 'Dentist',
            'business name': response.xpath('//div[@class="sales-info"]/h1/text()').extract(),
            'street': response.xpath('//p[@class="address"]/span/text()').extract_first(),
            'city': response.xpath('//p[@class="address"]').css('span:nth-child(2)::text').extract_first(),
            'state': response.xpath('//p[@class="address"]').css('span:nth-child(3)::text').extract_first(),
            'zip': response.xpath('//p[@class="address"]').css('span:nth-child(4)::text').extract_first(),
            'phone': response.xpath('//p[@class="phone"]/text()').extract_first(),
            'accepted insurance': response.xpath('//article[@id="accepted-insurance"]/p/text()').extract_first(),
            'extra': response.xpath('//dd[@class="other-information"]/p/text()').extract(),
            'email': response.xpath('//a[@class="email-business"]/@href').extract()
            # 'image': response.xpath('//a[@class="media-thumbnail"]/img/@src').extract_first(),
        }