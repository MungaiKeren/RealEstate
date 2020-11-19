from django.shortcuts import render, get_object_or_404
from .models import Listing
from .choices import bedroom_choices, price_choices, county_choices
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
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }
    return render(request, 'listings/single_listing.html', context)

def search(request):

    qs_list = Listing.objects.order_by('-list_date')
    # keywords

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            qs_list = qs_list.filter(description__icontains=keywords)
    
    #city
    
    if 'city' in request.GET:
        city = request.GET['city']

        if city:
            qs_list = qs_list.filter(city__iexact=city)
    
    # county

    if 'county' in request.GET:
        county = request.GET['county']
        if county:
            qs_list = qs_list.filter(county__iexact=county)
    
    # bedrooms

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']

        if bedrooms:
            qs_list = qs_list.filter(bedrooms__lte=bedrooms)
    
    # prices
    if 'price' in request.GET:
        price = request.GET['price']

        if price:
            qs_list = qs_list.filter(price__lte=price)



    context = {
        'county_choices': county_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': qs_list,
    }
    return render(request, 'listings/search.html', context)