from django.contrib import admin
from .models import Post, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'avatar')
    search_fields = ('name',)
    list_filter = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    search_fields = ('title', 'created_at')
    list_filter = ('title', 'created_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)