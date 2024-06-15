from django.contrib import admin
from .models import Post, Profile, Question


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    search_fields = ('user',)
    list_filter = ('user',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'created_at')
    search_fields = ('title', 'created_at')
    list_filter = ('title', 'status', 'created_at')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_t', 'status', 'author', 'created_at')
    search_fields = ('question_t', 'created_at')
    list_filter = ('question_t', 'status', 'created_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Question, QuestionAdmin)