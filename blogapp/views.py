from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, RegisterForm, CustomAuthenticationForm
from .models import Post
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'blogapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'blogapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/home.html', {'posts': posts})

@login_required
def teacher(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/teacher.html', {'posts': posts})

@login_required
def teacher_add_question(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/add_question.html', {'posts': posts})

@login_required
def teacher_add_test(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/add_test.html', {'posts': posts})

@login_required
def student(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/student.html', {'posts': posts})

@login_required
def student_past_questions(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/past_questions.html', {'posts': posts})

@login_required
def student_subjects(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/subjects.html', {'posts': posts})

# @login_required
def blog(request):
    posts = Post.objects.all()
    
    if request.method == "POST":
        post_id = request.POST.get('post-id')
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
        
    return render(request, 'blogapp/blog.html', {'posts': posts})

@login_required
def post_blog(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('success')
        else:
            messages.error(request, 'Failed to create post. Please correct the errors below.')
    else:
        form = PostForm()
    return render(request, 'blogapp/post.html', {'form': form})

@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blogapp/post_detail.html', {'post': post})

@login_required
def success(request):
    return render(request, 'blogapp/success.html')
