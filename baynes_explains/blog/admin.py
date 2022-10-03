from django.contrib import admin

from .models import Post
class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'content']

admin.site.register(Post, BlogAdmin)