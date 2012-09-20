from django.shortcuts import render
from project.models import Project

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'project/detail.html', locals())

def index(request):
    return render(request, 'project/index.html', locals())
