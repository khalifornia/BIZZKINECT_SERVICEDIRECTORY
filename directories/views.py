from django.shortcuts import render, HttpResponse
from directories.models import Dentist
from .forms import InitialSearchForm, DentistSearchForm
from .utility import Search, Stack
from django.db.models import Q
from ast import literal_eval
import queue

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
