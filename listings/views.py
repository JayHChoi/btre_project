from django.shortcuts import render
from django.views import generic
from .models import Listing
from .choices import price_choices, bedroom_choices, state_choices


class ListingListView(generic.ListView):
    ## model = Listing # No need when 'get_queryset' is overriden
    template_name = 'listings/listings.html'
    paginate_by = 6

    def get_queryset(self):
        return Listing.objects.order_by('-list_date').filter(is_published=True)


class ListingDetailView(generic.DetailView):
    model = Listing
    template_name = 'listings/listing.html'


class SearchView(generic.ListView):
    ## model = Listing # This is exactly the same as >> queryset = Listing.objects.all()
    template_name = 'listings/search.html'

    def get_queryset(self):
        """
        Replace or modify the default attribute 'queryset'
        The 'self.listings' below is a local variable inside the function
        There is no need to pass it to the context because, by default, it's passed as 'object_list'
        """
        self.listings = Listing.objects.order_by('-list_date')
        # Keywords
        if 'keywords' in self.request.GET:
            keywords = self.request.GET['keywords']
            if keywords:
                self.listings = self.listings.filter(
                    description__icontains=keywords)

        # City
        if 'city' in self.request.GET:
            city = self.request.GET['city']
            if city:
                self.listings = self.listings.filter(
                    city__iexact=city)

        # State
        if 'state' in self.request.GET:
            state = self.request.GET['state']
            if state:
                self.listings = self.listings.filter(
                    state__iexact=state)

        # Bedrooms
        if 'bedrooms' in self.request.GET:
            bedrooms = self.request.GET['bedrooms']
            if bedrooms:
                self.listings = self.listings.filter(
                    bedrooms__lte=bedrooms)

        # Price
        if 'price' in self.request.GET:
            price = self.request.GET['price']
            if price:
                self.listings = self.listings.filter(
                    price__lte=price)
        return self.listings

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state_choices'] = state_choices
        context['price_choices'] = price_choices
        context['bedroom_choices'] = bedroom_choices
        context['values'] = self.request.GET
        return context
