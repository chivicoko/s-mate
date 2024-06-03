from django.urls import path
from .views import frontpage, post_detail, upload_profile, profile_success, post_blog

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('post/', post_blog, name='post_blog'),
    path('upload/', upload_profile, name='upload_profile'),
    path('upload/success/', profile_success, name='profile_success'),
    path('<slug:slug>/', post_detail, name='post_detail'),
]