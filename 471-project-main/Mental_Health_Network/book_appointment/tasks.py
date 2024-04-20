#from django.utils import timezone
#from background_task import background
#from django.core.mail import send_mail
#from .models import Appointment


#def send_reminder_email(appointment_id, subject, message, recipient_list):
    #appointment = Appointment.objects.get(id=appointment_id)
    #appointment_datetime = appointment.date_time

    #reminder_1_day_before = appointment_datetime - timezone.timedelta(days=1)
    #reminder_1_hour_before = appointment_datetime - timezone.timedelta(hours=1)

    #now = timezone.now()
    #if now == reminder_1_day_before:
        #send_mail(subject, message, 'salmanpasha3011@gmail.com', recipient_list)
    #elif now == reminder_1_hour_before:
        #send_mail(subject, message, 'salmanpasha3011@gmail.com', recipient_list)