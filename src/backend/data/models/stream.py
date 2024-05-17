from django.db import models
from . import Unit

class Stream(models.Model):
    name = models.CharField(max_length=100)
    from_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, related_name='from_unit')
    to_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, related_name='to_unit')