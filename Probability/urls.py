"""Probability URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from abc import abstractproperty

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from blog.views import login_user, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_form', TemplateView.as_view(template_name='login.j2')),
    path('', TemplateView.as_view(template_name='index.j2')),
    path('test', TemplateView.as_view(template_name='index.j2')),
    path('user_login', login_user),
    path('logout/', logout_user)
    #path('/create_post'),
    #path('polls/<int:poll_id>')
]
