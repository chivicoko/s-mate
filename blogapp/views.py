from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, RegisterForm
from .models import Post
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'blogapp/register.html', {'form': form})

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
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'blogapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('frontpage')

def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/frontpage.html', {'posts': posts})

# @login_required
def post_blog(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            messages.error(request, 'Failed to create post. Please correct the errors below.')
    else:
        form = PostForm()
    return render(request, 'blogapp/post.html', {'form': form})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blogapp/post_detail.html', {'post': post})

def success(request):
    return render(request, 'blogapp/success.html')
