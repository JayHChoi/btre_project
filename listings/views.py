from django.shortcuts import render
from django.views import generic
from .models import Listing


class ListingListView(generic.ListView):
    model = Listing
    template_name = 'listings/listings.html'
    paginate_by = 6

    def get_queryset(self):
        return Listing.objects.order_by('-list_date').filter(is_published=True)

class ListingDetailView(generic.DetailView):
    model = Listing
    template_name = 'listings/listing.html'

def search(request):
    return render(request, 'listings/search.html')