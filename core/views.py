from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all() # Saare projects database se uthao
    return render(request, 'home.html', {'projects': projects})