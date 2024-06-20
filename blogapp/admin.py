from django.contrib import admin
from .models import Post, Profile, Question


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'avatar')
    search_fields = ('id', 'user',)
    list_filter = ('id', 'user',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'author', 'created_at')
    search_fields = ('id', 'title', 'created_at')
    list_filter = ('id', 'title', 'status', 'created_at')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_t', 'status', 'author', 'created_at')
    search_fields = ('id', 'question_t', 'created_at')
    list_filter = ('id', 'question_t', 'status', 'created_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Question, QuestionAdmin)