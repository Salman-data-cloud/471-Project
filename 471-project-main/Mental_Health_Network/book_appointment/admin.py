from django.contrib import admin
from .models import *

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'doctor', 'counselor', 'date', 'time']
    search_fields = ['user__username', 'doctor__name', 'counselor__name']
    list_filter = ['date', 'time']

# Register your models here.
