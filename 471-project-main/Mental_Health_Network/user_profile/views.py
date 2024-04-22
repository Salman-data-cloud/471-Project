from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
# Create your views here.
def profile(request):
    # user_profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html')

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
def doctor_white_view(request):
    return render(request, 'doctor_white.html')
def blog_writing_view(request):
    return render(request, 'blogs.html')
