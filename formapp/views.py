# views.py in formapp app
from django.shortcuts import render
from django.http import JsonResponse
from .models import Project

def index(request):
    return render(request, 'index.html')

from django.http import JsonResponse

def save_project(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')

        # Check if project name is empty
        if not project_name.strip():
            return JsonResponse({'success': False, 'message': 'Please enter a project name'}, status=400)

        if Project.objects.filter(name=project_name).exists():
            return JsonResponse({'success': False, 'message': 'Project name already used'}, status=400)
        else:
            Project.objects.create(name=project_name)
            return JsonResponse({'success': True, 'message': 'Project name saved successfully!!'})

    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)
