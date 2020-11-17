from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6) # shows 6 listings per page

    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)

    context = {
        'listings': paged_listings,
    }
    return render(request, 'listings/listings.html', context)

def single_listing(request, listing_id):
    return render(request, 'listings/single_listing.html')

def search(request):
    return render(request, 'listings/search.html')