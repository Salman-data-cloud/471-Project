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
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.db import transaction
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required

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
    return str(random.randint(1000,9999))

def send_otp(user,otp):
    subject = 'Password Reset Code'
    message = f'Your password reset OTP is: {otp}'
    sender = 'md.salman.pasha@g.bracu.ac.bd'
    receiver = user.email_address
    send_mail(subject,message,sender,receiver)

def forgot_password(request):
    if request.method == 'POST':
        email_address = request.POST.get('email_address')
        user = UserLoginAuth.objects.get(email_address = email_address)
        if user.DoesNotExist:
            messages.error(request, 'User does not exist with this email.')
            return redirect('/forgot_pass')
        
        otp =generate_otp()
        user.otp_code = otp
        user.save()

        send_otp(user,otp)
        
        messages.info(request, 'Kindly check your inbox for one-time password. Check the spam folder if not in inbox.')

    return render(request, 'forgot_pass.html')    

