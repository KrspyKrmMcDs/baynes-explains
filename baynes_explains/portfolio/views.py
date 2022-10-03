from django.shortcuts import render
from .models import Project


def project_list(request):
    context = {
        'projects' : Project.objects.all()
    }
    return render(request, 'portfolio/project_list.html', context=context)

def project(request):
    pass