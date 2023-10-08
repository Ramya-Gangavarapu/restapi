from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views  # Import your custom registration view (if you've created one)
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', views.register_view, name='register'),  # Use the appropriate view function
    path('', views.homepage_view, name='homepage'),  # This is the URL pattern for the homepage
    path('', views.homepage_view, name='homepage')
]