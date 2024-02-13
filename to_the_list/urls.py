"""
URL configuration for to_the_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user_authentication import views as user_auth_views
from shopping_list import views as shopping_list_views
# Import input_form_view from shopping_list app's views
from shopping_list.views import input_form_view

urlpatterns = [
    path('', user_auth_views.home, name='home'),  # Add home URL pattern
    path('about/', user_auth_views.about,
         name='about'),  # Add about URL pattern
    path("accounts/", include("allauth.urls")),
    path("user-authentication/test-auth/",
         user_auth_views.test_authentication, name='test_authentication'),
    path('shopping_list/', shopping_list_views.shopping_list_view,
         name='shopping_list'),
    path('admin/', admin.site.urls),
    # Add URL pattern for input_form_view
    path('input_form/', input_form_view, name='input_form'),
]

# path('', include('to_the_list.urls')),
