from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListingListView.as_view(), name='listings'),
    path('<int:pk>/', views.ListingDetailView.as_view(), name='listing'),
    path('search/', views.SearchView.as_view(), name='search'),
]
