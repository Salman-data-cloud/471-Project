from django.db import models
from django.contrib.auth import get_user_model

class Doctor(models.Model):

    CATEGORY_CHOICES = [('Psychologist', 'Psychologist'),
                ('Psychiatrist', 'Psychiatrist'),]

    name = models.CharField(max_length = 200)
    authorized_id = models.CharField(max_length = 10, unique = True)
    qualifications = models.TextField()
    total_experience = models.PositiveIntegerField()
    consultation_days = models.CharField(max_length = 500)
    consultation_time = models.CharField(max_length = 250)
    off_days = models.CharField(max_length = 100)
    appointment_fees = models.DecimalField(max_digits =10, decimal_places=2) 
    category = models.CharField(max_length = 20, choices = CATEGORY_CHOICES, default = 'Psychologist')
    def __str__(self):
        return self.name
    
class Counselor(models.Model):

    name = models.CharField(max_length = 200)
    authorized_id = models.CharField(max_length = 10, unique = True)
    qualifications = models.TextField()
    total_experience = models.PositiveIntegerField()
    consultation_days = models.CharField(max_length = 500)
    consultation_time = models.CharField(max_length = 250)
    appointment_fees = models.DecimalField(max_digits =10, decimal_places=2)

    def __str__(self):
        return self.name