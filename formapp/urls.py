from django.urls import path
from .views import index, save_project, validate_project_name, save_draggable_input

urlpatterns = [
    path('', index, name='index'),
    path('save_project/', save_project, name='save_project'),
    path('validate_project_name/', validate_project_name, name='validate_project_name'),
    path('save_draggable_input/', save_draggable_input, name='save_draggable_input'),
]
