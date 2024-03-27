from django.shortcuts import render
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def doctor_directory(request):

    psychologists = Doctor.objects.filter(category = 'Psychologist')
    psychiatrists = Doctor.objects.filter(category = 'Psychiatrist')
    counselors = Counselor.objects.all()

    return render(request, 'doctor_directory.html', {'psychologists':psychologists, 'psychiatrists':psychiatrists, 'counselors':counselors})


