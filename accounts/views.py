from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from django.contrib import messages, auth
from django.contrib.auth.models import User


class RegisterView(TemplateView):
    template_name = 'accounts/register.html'

    def post(self, request, *args, **kwargs):
        # Register User
        # messages.error(request, 'Testing error message')
        # return redirect('register')
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            # Login after register
            # auth.login(request, user)
            # messages.success(request, 'You are now logged in')
            # return redirect('index')
            user.save()
            messages.success(request, 'You are now registered!')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')


class LoginView(TemplateView):
    template_name = "accounts/login.html"

    def post(self, request, *args, **kwargs):
        # Login User
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')


class DashboardView(TemplateView):
    template_name = "accounts/dashboard.html"
    model = User


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
