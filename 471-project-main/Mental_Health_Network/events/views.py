from django.shortcuts import render

# Create your views here.
from .models import SeminarsConferences, Workshop

def upcoming_events(request):
    return render(request, 'upcoming_events.html')

def seminars(request):
    seminars = SeminarsConferences.objects.all()
    return render(request, 'seminars.html', {'seminars': seminars})

def workshops(request):
    workshops = Workshop.objects.all()
    return render(request, 'workshops.html', {'workshops': workshops})