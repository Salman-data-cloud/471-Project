from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import Appointment
#from .tasks import send_reminder_email

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['date']
            selected_time = form.cleaned_data['time']

            if not Appointment.objects.filter(date=selected_date, time=selected_time).exists():
                appointment = form.save()

                #send_reminder_email.delay(
                #appointment_id=appointment.id,
                #subject='Appointment Reminder',
                #message='Your appointment is coming up soon.',
                #recipient_list=[appointment.user.email])
                return redirect('payments_page')
            else:
                error_message = "This time slot is already booked. Please choose another time."
                return render(request, 'appointments/book_appointment.html', {'form': form, 'error_message': error_message})
        else:
            # Form is not valid, render the form with errors
            form = AppointmentForm()
    else:
        # GET request, initialize an empty form
        form = AppointmentForm()
    
    return render(request, 'book_appointment.html', {'form': form})

#def appointment_success(request):
    #return render(request, 'appointment_success.html')
            