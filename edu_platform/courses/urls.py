from django.urls import path
from . import views

app_name = 'courses'  # Add this line for namespacing
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
]
