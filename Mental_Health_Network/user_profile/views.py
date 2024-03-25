from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
# Create your views here.
def profile(request):
    # user_profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html')