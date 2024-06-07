from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')
    created_at = models.DateTimeField(auto_now_add=True, )
    # created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created_at',)
