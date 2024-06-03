from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile, Post


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/frontpage.html', {'posts': posts})

def post_blog(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProfileForm()
    return render(request, 'blogapp/post.html', {'form': form})

def post_detail(request, slug):
    return render(request, 'blogapp/post_detail.html')

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