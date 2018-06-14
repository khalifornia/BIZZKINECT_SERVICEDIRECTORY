from django.shortcuts import render, HttpResponse
from directories.models import Dentist
from .forms import InitialSearchForm, DentistSearchForm
from .utility import Search, Stack
from django.db.models import Q
from ast import literal_eval
import queue

from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from scrapyd_api import ScrapydAPI


scrapyd = ScrapydAPI('http://127.0.0.1:6800')

# takes search category as argument, returns list of form field keys associated with given category
def sub_category_switcher(category):
    switcher = {
        'Contractor' : ['contractor_category'],
        'Dentist' : ['insurance'],
        'Lawyer' : ['None'],
        'Restaurant' : ['None'],
        
    }
    return switcher.get(category)


# url: /
# homepage of bizzkinect.com
# handles search form and search results
def index(request):
    result = Dentist.objects.all()  # grab all listings
    form = InitialSearchForm(request.POST)  # Grabs (submitted) form data

    # if recieves a POST request, that means the form has been submitted,
    # and the data must be processed
    if request.method == 'POST':

        # Checks if form is valid, allows you to use form.cleaned_data
        # which checks for malicious submissions, incorrect submissions,
        # incorrectly formatted submissions, ensures requred fields aren't blank, etc.
        if form.is_valid():
            search_terms = form.cleaned_data['search_terms']
            category = form.cleaned_data['category']
            location = form.cleaned_data['location']
            # If search is empty
            if form.cleaned_data['search_terms'] != '':


            # sets search variable equal to the result set of the search query
                search = Dentist.objects.filter(
                    (Q(location__icontains=location) &
                    Q(yp_category__icontains=category)) &
                    (Q(name__icontains=search_terms) |
                    Q(yp_city__icontains=search_terms) |
                    Q(yp_extra_info__icontains=search_terms) |
                    Q(yp_category__icontains=search_terms) |
                    Q(search_tree__icontains=search_terms)) 
                )[:6]
            else:

                search = Dentist.objects.filter(
                    Q(location__icontains=location) &
                    Q(yp_category__icontains=category)
                )[:6]


            # dict to be returned in render response
            context = {
                'search': search,
                'form': InitialSearchForm(),
                'dentist_search_results': True,
            }
            # returns search_results page with context from above (search results, new blank form)
            return render(request, 'directories/index.html', context)
    else:

        form = InitialSearchForm()

        # returns empty form on first page load
    return render(request, 'directories/index.html', {'form': form,  'initial_search': True})

# Scrapy yellowpages
# /scrape/<source>/<search_terms>/<city>/<state>
@csrf_exempt
def scrape(request, source, search_terms, city, state, page_range, password):
    if password == 'am_ghey':
        meta_info = {

            "source": source,
            "search_terms": search_terms,
            "city": city,
            "state": state
        }

        # Unique ID for each scraper instance
        unique_id = str(uuid4())

        #Universally recognized citystate string
        universal_citystate = meta_info['city'] +'-' + meta_info['state']

        # Can be accessed from anywhere in scraper
        settings = {
            'universal_citystate': universal_citystate,
            'unique_id': unique_id,  # unique ID for each record for DB
            'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
        }
        for page_counter in range(int(page_range)):
            
            # schedule Scrapyd task
            task = scrapyd.schedule('default', 'yellow_pages_spider', settings=settings, city=meta_info['city'], state=meta_info['state'], search_terms=meta_info['search_terms'], page_counter=page_counter)
        return JsonResponse({'task_id': task, 'unique_id': unique_id, 'universal_citystate': universal_citystate, 'status': 'started'})
    elif password == 'sboj':
        jobs = scrapyd.list_jobs('default')
        return HttpResponse(jobs['running'])
    else:
        return HttpResponse("Bad Password")


# # /vendor/create/$userid
# # create new vendor user
# # takes TS User object
# def create_vendor(request):

# # /vendor/update/$userid
# # update vendor user
# # takes TS User Object
# def update_vendor(request):

# #/vendor/delete/$userid
# # delete vendor user
# # Takes TS User object
# def delete_vendor(request):

# # /vendor/get/$userid
# # return vendor user
# # returns TS User object
# def get_vendors(request):
