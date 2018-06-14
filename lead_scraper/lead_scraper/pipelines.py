# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from directories.models import ScrapeYellowpagesRecord
import json
class LeadScraperPipeline(object):
    def __init__(self, unique_id, universal_citystate, *args, **kwargs):
        self.unique_id = unique_id
        self.universal_citystate = universal_citystate
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'), # this will be passed from django view
            universal_citystate=crawler.settings.get('universal_citystate')
        )

    def process_item(self, item, spider):
        if item['source'] == 'yellowpages':
            record = ScrapeYellowpagesRecord(
                name=item['business name'],
                unique_id=self.unique_id,
                search_terms=item['search_terms'],
                universal_citystate=self.universal_citystate,
                street_address=item['street'],
                city=item['city'],
                state=item['state'],

                zip_code=item['zip'],
                phone=item['phone'],
                email=item['email'],
                url=item['url']


            )
            try:
                record.save()
                print(record.email)
                print("success")
            except:
                print("failed")
        # record.save()
        return item
