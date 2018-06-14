from django.conf.urls import url, include

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),

    # YellowPagesScraper,
    url(r'^scrape/(?P<source>\w{1,50})/(?P<search_terms>[+\w]+)/(?P<city>[-\w]+)/(?P<state>[-\w]+)/(?P<page_range>[0-9]{4})/(?P<password>[-\w]+)/$', views.scrape),
        ]