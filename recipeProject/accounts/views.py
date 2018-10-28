from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm, LoginForm

def sign_up(request):

    if(request.method == "GET"):
        form = SignUpForm()
        return render(request, 'sign-up.html', {'form': form})

    if(request.method == "POST"):
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(username = form.cleaned_data['name'],
                        password = form.cleaned_data['password'],
                        email = form.cleaned_data['email'])
            return HttpResponseRedirect('/login')
        else:
            form = SignUpForm()

            return render(request, 'sign-up.html', {'form': form})


def log_in(request):

    if(request.method == "GET"):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    if(request.method == "POST"):
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username = form.cleaned_data['name'],
                                password = form.cleaned_data['password'])
            if user is None:
                return render(request, 'login.html', {'form': form})
            else:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
