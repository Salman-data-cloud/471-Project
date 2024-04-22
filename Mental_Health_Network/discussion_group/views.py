from django.shortcuts import render
from django.http import HttpResponse
from discussion_group.templates import *

# Create your views here.

def home(request):
    return HttpResponse("Helo xyz")


def show_group(request):
    return render(request, "index.html")
