from django.shortcuts import render, get_object_or_404
from .models import Project,Skill

# Create your views here.

def homepage(request):
    projects = Project.objects
    skills = Skill.objects
    return render(request, 'projects/home.html', {'projects':projects,'skills':skills})

def detail(request,project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'projects': project_detail})