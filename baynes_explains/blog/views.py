from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name_suffix = '_update_form'


class PostDeleteView(DeleteView):
    model = Post
    success_url: reverse_lazy('post-list')


def index(request):
    return render(request, 'blog/index.html')
