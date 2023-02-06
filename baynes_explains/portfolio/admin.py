from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    fields = ['name', 'content', 'youtube_link']


admin.site.register(Project, ProjectAdmin)
