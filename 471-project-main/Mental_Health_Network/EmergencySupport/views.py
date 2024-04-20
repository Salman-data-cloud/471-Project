from django.shortcuts import render

# Create your views here.



from .models import EmergencySupportResource

def EmergencySupport(request):
    support_resource = EmergencySupportResource.objects.all()
    
    
    return render(request, 'emergencysupport.html', {'support_resources': support_resource})


