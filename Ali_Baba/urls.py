"""
URL configuration for Ali_Baba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from dj_rest_auth.views import (
    LoginView,
    LogoutView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Authentication urls
    path('auth/login/', LoginView.as_view(), name='rest_login'),
    path('auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('', include("Register.urls")),

    # Flights list
    path('', include("Internal_Flights.urls")),
    path('', include("International_Flights.urls")),

    # User profile
    path('', include("User_Dashboard.urls")),
]
