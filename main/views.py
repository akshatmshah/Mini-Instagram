from pyexpat.errors import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Profile


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out!")
    return redirect("insta:homepage")


def login_request(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("insta:user_profile")
            # return HttpResponseRedirect(reverse('insta:user_profile',
            #                                     kwargs={'username': username}))
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'profile.html', {'form': form})
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


def homepage(request):
    return redirect('insta:login')


def get_user_profile(request, username):
    user = get_object_or_404(User, pk=username)
    profile = Profile.objects.get(user=user)
    return render(request, "profile.html", {"profile": profile})
