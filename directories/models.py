from django.db import models

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

    lead_type=models.CharField(max_length=50, choices=LEAD_TYPE_CHOICES)
    lead_name=models.CharField(max_length=512)


class SourceScrapeYellowpages(Lead):
    class Meta:
        db_table = '_source_scrape_yellowpages'
    date_created=models.CharField(max_length=256)
    street_address=models.CharField(max_length=256)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    description=models.CharField(max_length=1054)
    email=models.CharField(max_length=100)
    search_terms=models.CharField(max_length=200)
    extra_info=models.CharField(max_length=200, blank=True, null=True)
    url=models.CharField(max_length=200)
    product_terms=models.CharField(max_length=1024)
    




# class SourcePhoneInbound(Lead):
#     pass

# class SourcePhoneOutbound(Lead):
#     pass

# class SiteSubmission(Lead):
#     pass




