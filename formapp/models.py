# models.py
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)


class DraggableInput(models.Model):
    input_field_id = models.CharField(max_length=100, default='')
    data = models.CharField(max_length=255)
    x_axis = models.FloatField()
    y_axis = models.FloatField()
    

    def __str__(self):
        return self.data