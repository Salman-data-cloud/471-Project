from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from .forms import ProfileForm
from django.contrib.auth.models import User



def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_detail')  
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})

def profile_detail(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile_detail.html', {'profile': profile})

#def update_profile(request):
    #try:
        #profile = Profile.objects.get(user=request.user)
    #except ObjectDoesNotExist:
        #return redirect('create_profile')
    #if request.method == 'POST':
        #form = ProfileForm(request.POST, request.FILES, instance=profile)
        #if form.is_valid():
            #form.save()
            #return redirect('profile_detail')  # Redirect to profile detail page
    #else:
        #form = ProfileForm(instance=profile)
    #return render(request, 'update_profile.html', {'form': form})

def send_email_to_client():
    print("Sending email to client")
    subject = f"subject:user so and so booking an appoitnment"
    message = f"message: this user wants to book an appointment at so and so time"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["ridwanul.haque@g.bracu.ac.bd"]
    send_mail(subject,message,from_email,recipient_list)
def send_email_view(request):
    if request.method == 'POST':
        send_email_to_client()
        return redirect('email_sent')  # Assuming 'email_sent' is the name of your success page URL
    return JsonResponse({'message': 'Method not allowed'}, status=405)
def email_sent_view(request):
    return render(request, 'email_sent.html')

