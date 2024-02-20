# views.py in formapp app
from django.shortcuts import render
from django.http import JsonResponse
from .models import Project,DraggableInput

def index(request):
    return render(request, 'index.html')

def save_project(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        if Project.objects.filter(name=project_name).exists():
            return JsonResponse({'message': 'Name already used'}, status=400)
        else:
            Project.objects.create(name=project_name)
            return JsonResponse({'message': 'Project name saved successfully!!'})
    return JsonResponse({'message': 'Invalid request'}, status=400)

def validate_project_name(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        exists = Project.objects.filter(name=project_name).exists()
        return JsonResponse({'exists': exists})
    return JsonResponse({'exists': False})

def save_draggable_input(request):
    if request.method == 'POST':
        data = request.POST.getlist('data[]')
        x_axis = request.POST.getlist('x_axis[]')
        y_axis = request.POST.getlist('y_axis[]')
        input_field_ids = request.POST.getlist('input_field_id[]')
        label_names = request.POST.getlist('label_name[]')
        label_ids = request.POST.getlist('label_id[]')
        label_x_axis = request.POST.getlist('label_x_axis[]')  # New field for label x-axis
        label_y_axis = request.POST.getlist('label_y_axis[]')  # New field for label y-axis

        # Loop through the received data and save each draggable input field
        for i in range(len(data)):
            draggable_input = DraggableInput.objects.create(
                data=data[i],
                x_axis=x_axis[i],
                y_axis=y_axis[i],
                input_field_id=input_field_ids[i],
                label_name=label_names[i],
                label_id=label_ids[i],
                label_x_axis=label_x_axis[i],  # Include label x-axis value
                label_y_axis=label_y_axis[i]   # Include label y-axis value
            )
            draggable_input.save()

        return JsonResponse({'message': 'Data submitted successfully!'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)