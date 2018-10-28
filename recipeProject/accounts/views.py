from django.shortcuts import render
from django.http import HttpResponse
from .models import Account
from django.template import loader
from django.http import Http404

def sign_up(request):

    if(request.method == "GET"):
        return render(request, 'sign-up.html')


def log_in(request):

    if(request.method == "GET"):
        return render(request, 'login.html')
