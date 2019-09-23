from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import redirect


# Create your views here.


def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponsePermanentRedirect('/')
    else:
        return HttpResponsePermanentRedirect('/')


def logout_user(request):
    logout(request)
    return Redirect('')
