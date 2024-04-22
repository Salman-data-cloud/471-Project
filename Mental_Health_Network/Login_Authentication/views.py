import random
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from django.db import transaction
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
import string
import random 
@login_required(login_url='/login/')

def home(request):
    
    return render(request, 'home.html')




def login_page(request):
    
    
    
    if request.method == 'POST':
        

        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, 'Invalid Username or Password!')
            return redirect('/login/')
        else:
            login(request, user)
            next_path = request.GET.get('next','home')
            return redirect(next_path)

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')

def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_address = request.POST.get('email_address')
        phone_number = request.POST.get('phone_number')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():

        
            messages.error(request, "Username already exists. Try another one.")
            return redirect('/register/')
        if User.objects.filter(email_address=email_address).exists():
            messages.error(request, 'Email already registered')
            return redirect('/register/')
        with transaction.atomic():
            user = UserLoginAuth.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email_address = email_address,
                username = username,
                phone_number = phone_number,
                password = password
                
            )
        
        
       

        messages.success(request, "Account Created Successfully!")
        return redirect('/register/')
    
    return render(request, 'register.html')


def generate_otp():
    # Generate a 6-digit random OTP
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            
            return render(request, 'forgot_password.html', {'error_message': 'User with this email does not exist'})
        
        
        otp = generate_otp()

        
        request.session['password_reset_otp'] = otp
        request.session['password_reset_email'] = email

        # Send OTP via email
        email_subject = 'Password Reset OTP'
        email_message = f'Hi {user.username},\n\nYour OTP for password reset is: {otp}'
        sender_email = settings.EMAIL_HOST_USER
        send_mail(email_subject, email_message, sender_email, [email])

        return render(request, 'verify_otp.html')
    
    return render(request, 'forgot_password.html')

def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('password_reset_otp')
        if entered_otp == stored_otp:
            # OTP is correct, allow the user to reset their password
            email = request.session.get('password_reset_email')
            del request.session['password_reset_otp']  # Clear OTP from session
            del request.session['password_reset_email']  # Clear email from session
            return render(request, 'reset_password.html', {'email': email})
        else:
            # OTP is incorrect, display error message
            messages.error(request, 'Invalid OTP. Please try again.')
            return redirect('forgot_password')

    return render(request, 'verify_otp.html')