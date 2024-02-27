from django.urls import path
from .views import index, save_project

urlpatterns = [
    path('', index, name='index'),
    path('save_project/', save_project, name='save_project'),
]
