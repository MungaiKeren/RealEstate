from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, county_choices, price_choices
from django.http import HttpResponse

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'county_choices': county_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, "pages/index.html", context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # get the sellor of the month
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtor
    }
    return render(request, 'pages/about.html', context)
