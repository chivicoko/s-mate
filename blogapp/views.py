from django.shortcuts import render, redirect
from .forms import ProfileForm, PostForm, RegisterForm
from .models import Profile, Post

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('frontpage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('frontpage')

def frontpage(request):
    posts = Post.objects.all()
    profiles = Profile.objects.all()
    return render(request, 'blogapp/frontpage.html', {'posts': posts, 'profiles': profiles})

@login_required
def post_blog(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PostForm()
    return render(request, 'blogapp/post.html', {'form': form})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blogapp/post_detail.html', {'post':post})

@login_required
def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProfileForm()
    return render(request, 'blogapp/upload_profile.html', {'form': form})

def success(request):
    return render(request, 'blogapp/success.html')