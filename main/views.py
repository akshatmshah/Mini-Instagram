from pyexpat.errors import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Profile, Post
from django.views import generic
from django.utils import timezone
from .forms import Post as PostForm


def logout_request(request):
    logout(request)
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
            username = User.objects.get(username=request.user)
            return HttpResponseRedirect('/%s/' % username.id)
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
            return redirect("insta:login")
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


def homepage(request):
    return redirect('insta:login')


def get_user_profile(request, username):
    user = get_object_or_404(User, pk=username)
    prof = Profile.objects.get_or_create(user=user)
    return render(request, "profile.html", {"profile": prof})


class Feed(generic.ListView):
    template_name = 'base.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


def create_post(request):
    form = PostForm
    if request.method == 'POST':
        postf = PostForm(request.POST)
        if postf.is_valid():
            profile = postf.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('insta:feed')
    return render(request, 'create.html', {'form': form})


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.user)
    post.delete()
    return redirect("insta:feed")
