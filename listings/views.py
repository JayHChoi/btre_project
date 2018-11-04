from django.shortcuts import render
from django.views import generic
from .models import Listing


class ListingListView(generic.ListView):
    model = Listing
    template_name = 'listings/listings.html'

# def index(request):
#     return render(request, 'listings/listings.html')

def listing(request, id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')