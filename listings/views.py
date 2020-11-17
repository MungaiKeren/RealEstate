from django.shortcuts import render
from .models import Listing

# Create your views here.
def listings(request):
    listings = Listing.objects.all()

    context = {
        'listings': listings,
    }
    return render(request, 'listings/listings.html', context)

def single_listing(request, listing_id):
    return render(request, 'listings/single_listing.html')

def search(request):
    return render(request, 'listings/search.html')