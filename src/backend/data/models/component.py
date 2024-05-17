from django.db import models
from . import Stream

class Component(models.Model):
    name = models.CharField(max_length=100)
    parent_stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    flowrate = models.DecimalField(max_digits=12, decimal_places=3, null=True)