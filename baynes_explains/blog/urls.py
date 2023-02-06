from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('posts', views.PostListView.as_view(), name='blog-list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='blog-detail'),
    path('create/', views.PostCreateView.as_view()),
    path('update/<int:pk>/', views.PostUpdateView.as_view()),
    path('delete/<int:pk>/', views.PostDeleteView.as_view())
]
