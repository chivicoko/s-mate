from django.shortcuts import render, redirect
from .forms import ProfileForm, PostForm
from .models import Profile, Post


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/frontpage.html', {'posts': posts})

def post_blog(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blogapp/post.html', {'form': form})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blogapp/post_detail.html', {'post':post})

def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_success')
    else:
        form = ProfileForm()
    return render(request, 'blogapp/upload.html', {'form': form})

def profile_success(request):
    return render(request, 'blogapp/profile_success.html')