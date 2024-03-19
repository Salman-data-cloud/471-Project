from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Event(models.Model):

    event_name = models.CharField(max_length = 500)
    event_date = models.CharField(max_length = 25)
    event_details = models.TextField()
    venue = models.TextField(default = 'Google Meet')

    def __str__(self):
        return self.event_name