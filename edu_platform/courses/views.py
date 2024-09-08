from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Course
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('courses:dashboard')
    return render(request, 'courses/login.html')

def dashboard_view(request):
    courses = Course.objects.all()
    return render(request, 'courses/dashboard.html', {'courses': courses})

def home_view(request):
    return redirect('courses:login')  # Redirect to the login page

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('courses:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'courses/signup.html', {'form': form})