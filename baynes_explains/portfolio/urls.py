from django.urls import path
from . import views

urlpatterns = [
    path('project_list/', views.project_list, name='portfolio-project_list'),
    path('project/', views.project, name='portfolio-project'),
]
