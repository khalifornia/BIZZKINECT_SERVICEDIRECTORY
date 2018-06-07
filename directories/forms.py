from django import forms
from directories.choices import *
import psycopg2


# Search form with only one universal search bar
class InitialSearchForm(forms.Form):




    search_terms = forms.CharField( max_length=400, required=False, widget=forms.TextInput(attrs={'placeholder': 'Optional keywords...'}))
    category = forms.ChoiceField(choices=CATEGORIES, required=True)
    location = forms.ChoiceField(choices=LOCATIONS, required=True)
    # DENTAL
    insurance = forms.ChoiceField(choices=HEALTH_INSURANCE_COMPANIES, required=False)

    # CONTRACTORS
    contractor_category = forms.ChoiceField(choices=CONTRACTOR_CATEGORIES, required=False)

    

# UNUSED
class DentistSearchForm(forms.Form):
    insurance = forms.ChoiceField(choices=HEALTH_INSURANCE_COMPANIES)