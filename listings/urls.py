from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListingListView.as_view(), name='listings'),
    path('<int:id>/', views.listing, name='listing'),
    path('search/', views.search, name='search'),
]
