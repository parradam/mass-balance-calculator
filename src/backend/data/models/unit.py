from django.db import models
from . import Design

class Unit(models.Model):
    name = models.CharField(max_length=100)
    design = models.ForeignKey(Design, on_delete=models.CASCADE, related_name='units')