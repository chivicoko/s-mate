from django.urls import path
from .views import frontpage, post_detail, upload_profile, success, post_blog, register_view, login_view, logout_view

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('post/', post_blog, name='post_blog'),
    path('upload_profile/', upload_profile, name='upload_profile'),
    path('success/', success, name='success'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]