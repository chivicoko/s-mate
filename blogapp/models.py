from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import uuid


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'Draft', ('Draft')
        PUBLISHED = 'Published', ('Published')
        ARCHIVED = 'Archived', ('Archived')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    intro = models.TextField()
    body = models.TextField()
    status = models.CharField(max_length=100, choices=Status.choices, default=Status.DRAFT,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
        DRAFT = 'Draft', ('Draft')
        PUBLISHED = 'Published', ('Published')
        ARCHIVED = 'Archived', ('Archived')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question_t = models.TextField()
    answer_t = models.TextField()
    thumbnail = models.ImageField(upload_to='questions_thumbnails/', blank=True, null=True)
    status = models.CharField(max_length=100,choices=Status.choices,default=Status.DRAFT,)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_t
    
    class Meta:
        ordering = ('-created_at',)
