from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import PaymentForm
import random

@login_required
def payment_page(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            otp = random.randint(1000, 9999)
            print("Generated OTP:", otp)
            send_otp(str(form.cleaned_data['mobile_number']), otp)  
            request.session['otp'] = otp
            amount_float = float(form.cleaned_data['amount'])
            
            request.session['payment_data'] = {
                'bank_account_number': form.cleaned_data['bank_account_number'],
                'mobile_number': form.cleaned_data['mobile_number'],
                'amount': amount_float}
            return redirect('otp_verification')
        else:
            form = PaymentForm()
        return render(request, 'payments_page.html', {'form': form})
    else:
        form = PaymentForm()
        return render(request, 'payments_page.html', {'form': form})

@login_required
def otp_verification(request):
    if 'otp' not in request.session:
        return redirect('payment_page')
    if request.method == 'POST':
        otp_entered = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        if otp_entered == str(stored_otp):
            #del request.session['otp']
            return redirect('process_payment')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return redirect('otp_verification')
    return render(request, 'otp_verification.html')

@login_required
def process_payment(request):
    
    messages.success(request, 'Congratulations! Your payment is successful.')
    return render(request, 'success_page.html')

def send_otp(mobile_number, otp):
    print(f"Sending OTP {otp} to {mobile_number}")

