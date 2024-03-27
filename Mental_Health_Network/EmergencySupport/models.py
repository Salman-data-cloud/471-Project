from django.db import models

# Create your models here.
from django.db import models

class EmergencySupportResource(models.Model):
    organization_name = models.CharField(max_length=100)
    helpline_number = models.CharField(max_length=20)
    email = models.EmailField()
    additional_information = models.TextField(blank=True)

