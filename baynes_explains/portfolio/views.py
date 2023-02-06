from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Project


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'content', 'youtube_link']


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'content', 'youtube_link']
    template_name_suffix = '_update_form'


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = 'project-list'
