from django.urls import path
from .views import frontpage, teacher, student, blog, post_detail, success, post_blog, register_view, login_view, logout_view

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('teacher/', teacher, name='teacher'),
    path('student/', student, name='student'),
    path('blog/', blog, name='blog'),
    path('blog/new-post/', post_blog, name='post_blog'),
    path('success/', success, name='success'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]