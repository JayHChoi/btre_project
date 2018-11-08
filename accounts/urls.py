from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]