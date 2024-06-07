from django import forms
from .models import Profile, Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'avatar']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'thumbnail', 'intro', 'body']
