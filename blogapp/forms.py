from django import forms
from .models import Profile, Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'avatar']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'thumbnail', 'intro', 'body']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post slug'
            }),
            'thumbnail': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
            'intro': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter a brief introduction'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Enter the full content'
            }),
        }
