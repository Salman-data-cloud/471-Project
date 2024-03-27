from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import PaymentForm
import random
from django.utils import timezone
from django.template.loader import get_template
from .models import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse



@login_required
def payment_page(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            otp = random.randint(1000, 9999)
            print("Genertaed OTP:", otp)
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

    if 'payment_data' not in request.session:
        return redirect('payments_page')
    payment_data = request.session.get('payment_data', {})
    amount = payment_data.get('amount')
    if not amount:
        return redirect('payments_page')
    payment_date = timezone.now()

     
   
    messages.success(request, 'Congratulations! Your payment is successful.')
    return render(request, 'success_page.html', {'payment_date': payment_date})

def send_otp(mobile_number, otp):
    print(f"Sending OTP {otp} to {mobile_number}")


def generate_invoice(request):
    payment_data = request.session.get('payment_data',{})
    payment_date = timezone.now()
    template = get_template('invoice_template.html')
    context = {'payment_data':payment_data, 'payment_date':payment_date}
    html = template.render(context)

    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposation'] = 'attachment; filename = "invoice.pdf"'
    
    p = canvas.Canvas(response, pagesize = letter)
    p.drawString(100,750,'Invoice')
    p.drawString(100, 730, f"Date: {payment_date.strftime('%Y-%m-%d %H:%M:%S')}")
    p.drawString(100, 710, f"Bank Account Number: {payment_data.get('bank_account_number', '')}")
    p.drawString(100, 690, f"Mobile Number: {payment_data.get('mobile_number', '')}")
    p.drawString(100, 670, f"Amount: {payment_data.get('amount', '')}")
    p.save()

    return response 
