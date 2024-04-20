from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from Find_Doctor.models import *

User = get_user_model()

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['doctor', 'date', 'time']

