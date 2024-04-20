from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SeminarsConferences, Workshop

admin.site.register(SeminarsConferences)
admin.site.register(Workshop)