from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project-list'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('create/', views.ProjectCreateView.as_view()),
    path('update/<int:pk>/', views.ProjectUpdateView.as_view()),
    path('delete/<int:pk>/', views.ProjectDeleteView.as_view()),
]
