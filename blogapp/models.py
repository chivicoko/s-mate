from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DR', ('Draft')
        PUBLISHED = 'PB', ('Published')
        ARCHIVED = 'AR', ('Archived')

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    intro = models.TextField()
    body = models.TextField()
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.png', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ('-created_at',)


class Question(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DR', ('Draft')
        PUBLISHED = 'PB', ('Published')
        ARCHIVED = 'AR', ('Archived')

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    thumbnail = models.ImageField(upload_to='questions_thumbnails/', blank=True, null=True)
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT,)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)
