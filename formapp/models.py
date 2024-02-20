# models.py
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)


class DraggableInput(models.Model):
    input_field_id = models.CharField(max_length=100, default='')
    data = models.CharField(max_length=255)
    x_axis = models.FloatField()  # Stores both input fields' and labels' x-axis position
    y_axis = models.FloatField() 
    label_x_axis = models.FloatField(blank=True, null=True)  # New field for label x-axis position
    label_y_axis = models.FloatField(blank=True, null=True)  # New field for label y-axis position# Stores both input fields' and labels' y-axis position
    label_name = models.CharField(max_length=100, blank=True, null=True)  # New field for label name
    label_id = models.CharField(max_length=100, blank=True, null=True)    # New field for label id
    
    def __str__(self):
        return self.data
