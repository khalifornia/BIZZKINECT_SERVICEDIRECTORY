from django.db import models

from django.utils import timezone

class Dentist(models.Model):

    # name of office
    name=models.CharField(max_length=100)

    # City, state tuple in format: (HOU, TX)
    location=models.CharField(max_length=9, blank=True, null=True)

    # Category searched for in yellowpage scraper
    yp_category=models.CharField(max_length=100, null=True, blank=True)

    # Dict of subcategories and other misc fields important for search filtering
    search_tree=models.TextField(null=True, blank=True)
    email_data=models.TextField(null=True, blank=True)
    # subcategory from yellowpages
    yp_sub_category=models.CharField(max_length=5000, null=True, blank=True)
    insurance=models.CharField(max_length=512, null=True)
    phone=models.CharField(max_length=20, null=True)
    yp_street_address=models.CharField(max_length=100, blank=True, null=True)
    yp_city=models.CharField(max_length=30, blank=True, null=True)
    yp_state=models.CharField(max_length=3, blank=True, null=True)
    yp_zip_code=models.CharField(max_length=6, blank=True, null=True)

    # logo/image provided
    yp_image=models.CharField(max_length=256, blank=True, null=True)

    # description of company (dentist) on manta
    yp_description=models.TextField(blank=True, null=True)
    yp_email=models.TextField(blank=True, null=True)
    yp_extra_info=models.TextField(blank=True, null=True)
    # keywords associated with this dentist, provided by Manta.com
    yp_product_terms=models.TextField(max_length=512, blank=True, null=True)
    yp_url=models.CharField(max_length=512, blank=True, null=True)
    unionreporters_description=models.TextField(blank=True, null=True)
    current_dentists=models.TextField(blank=True, null=True)
    facebook_url=models.CharField(max_length=256, blank=True, null=True)
    twitter_url=models.CharField(max_length=256, blank=True, null=True)


    # TODO: replace unionreporters_raw_address with individual columns below it by parsing it
    unionreporters_raw_address = models.CharField(max_length=1024, blank=True, null=True)
    # unionreporters_street_address=models.CharField(max_length=100)
    # unionreporters_city=models.CharField(max_length=100)
    # unionreporters_state=models.CharField(max_length=100)
    # unionreporters_zip=models.CharField(max_length=100)

    unionreporters_location=models.CharField(max_length=512, blank=True, null=True)
    unionreporters_categories=models.TextField(blank=True, null=True)
    unionreporters_url=models.CharField(max_length=512, blank=True, null=True)

    unionreporters_phone=models.CharField(max_length=10, blank=True, null=True)


class Lead(models.Model):
    class Meta:
        db_table = '_leads'

    LEAD_TYPE_CHOICES = (
        ('company', 'Company'),
        ('person', 'Person'),
        )
    DATA_TYPE_CHOICES = (
        ('source', 'Source'),
        ('behavior', 'Behavior'),
        ('meta', 'Meta'),
    )
    lead_type=models.CharField(max_length=50, choices=LEAD_TYPE_CHOICES)
    data_type=models.CharField(max_length=50, choices=DATA_TYPE_CHOICES)
    data_table=models.CharField(max_length=100)
    data_table_fk=models.BigIntegerField()
    lead_name=models.CharField(max_length=512)


class ScrapeYellowpagesRecord(models.Model):
    class Meta:
        db_table = '_source_scrape_yellowpages'

    date_created = models.DateTimeField(default=timezone.now)
    unique_id = models.CharField(max_length=100, null=True)
    universal_citystate=models.CharField(max_length=100)
    street_address=models.CharField(max_length=256)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    description=models.CharField(max_length=1024)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=25)
    search_terms=models.CharField(max_length=200)
    extra_info=models.CharField(max_length=200, blank=True, null=True)
    url=models.CharField(max_length=200)
    product_terms=models.CharField(max_length=1024)


    def __str__(self):
        return self.unique_id


# class ScrapeSourceRecord():
#
#     def __init__(self, source, meta_info):
#         self.source = source
#         self.meta_info = meta_info
#
#
#     def run_scraper(self):
#
#         process = CrawlerRunner({
#             'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#         })
#
#         if self.source == 'yellowpages':
#             print("works")
#             try:
#                 process.crawl(YellowPagesSpider)
#                 process.stop()
#             except Exception as err:
#                 print(err)
#
#         reactor.run()



# Scrapes yellowpages given search terms and location as parameters
# class YellowPagesSpider(scrapy.Spider):
#     name = "yellow_pages"
#     def __init__(self, *args, **kwargs):
#         super(YellowPagesSpider, self).__init__(*args, **kwargs)
#         self.meta_info = kwargs.get('meta_info')
#
#     def start_requests(self):
#
#         url = 'https://www.yellowpages.com/search?search_terms=' + self.meta_info['search_terms'] + \
#                 '&geo_location_terms=' + self.meta_info['city'] + '%2C+' + self.meta_info['state'] + '&page=3'
#
#             # url = 'https://www.yellowpages.com/search?search_terms=Dentist&geo_location_terms=Phoenix%2C+AZ&page=' + str(self.page_id)
#         yield scrapy.Request(url=url, callback=self.parse_results)
#
#
#     def parse_results(self, response):
#         url_list = []
#         for dentist in response.css('div.search-results div.result'):
#             url_list.append("https://www.yellowpages.com" + dentist.xpath('.//a[@class="business-name"]/@href').extract_first())
#         for url in url_list:
#
#             yield scrapy.Request(url=url, callback=self.parse_listing, meta={'url': url})

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

# class SourcePhoneInbound(Lead):
#     pass

# class SourcePhoneOutbound(Lead):
#     pass

# class SiteSubmission(Lead):
#     pass




