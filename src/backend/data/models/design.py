from django.db import models

class Design(models.Model):
    name = models.CharField(max_length=100)
    flowrate_units = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)