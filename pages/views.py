from django.views import generic
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices

# def index(request):
#     return render(request, 'pages/index.html')


class IndexView(generic.TemplateView):
    template_name = 'pages/index.html'
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listings'] = self.listings
        context['state_choices'] = state_choices
        context['price_choices'] = price_choices
        context['bedroom_choices'] = bedroom_choices
        return context


class AboutView(generic.TemplateView):
    template_name = 'pages/about.html'
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['realtors'] = self.realtors
        context['mvp_realtors'] = self.mvp_realtors
        return context
