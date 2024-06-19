from django.urls import path
from .views import home, fetch_jobs_view, teacher, new_question, add_test, questions_tests, past_questions, subjects, blog, post_detail, success, new_blog_post, register_view, login_view, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('fetch-jobs/', fetch_jobs_view, name='fetch_jobs_view'),
    path('teacher/', teacher, name='teacher'),
    path('teacher/new_question/', new_question, name='new_question'),
    path('teacher/add_test/', add_test, name='add_test'),
    path('questions_tests/', questions_tests, name='questions_tests'),
    path('questions_tests/past_questions', past_questions, name='past_questions'),
    path('questions_tests/subjects', subjects, name='subjects'),
    path('blog/', blog, name='blog'),
    path('blog/new_blog_post/', new_blog_post, name='new_blog_post'),
    path('success/', success, name='success'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]