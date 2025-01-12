"""
URL configuration for Mental_Health_Network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Login_Authentication.views import *
from Support_Group.views import *
from user_profile.views import  create_profile, profile_detail
from django.conf import settings
from django.conf.urls.static import static
from Find_Doctor.views import *
from event_manager.views import *
from Support_Group.views import reply_message
from event_manager.views import join_event
from payments.views import *
from resources.views import *
from book_appointment.views import *
from EmergencySupport.views import *
from discussion_group.views import *
from events.views import upcoming_events, seminars, workshops
from feedback.views import *
from chatbot.views import *
from policy.views import *
#from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', login_page, name= 'login_page'),
    path('register/', register, name= 'register'),
    path('logout/', logout_user, name='logout'),
    path('forgot_pass/',forgot_password, name='forgot_password'),
    path('home/', home, name = 'home'),
    path('create_profile/', create_profile, name = 'create_profile'),
    path('profile_detail/', profile_detail, name = 'profile_detail'),
    path('support_app/', support_app , name = 'support_app'),
    path('support_detail/<int:group_id>/', support_detail, name = 'support_detail'),
    path('user_greeting/', user_greeting, name = 'user_greeting'),
    path('send_message/<int:group_id>/', send_message, name='send_message'),
    path('doctor_directory/', doctor_directory, name = 'doctor_directory' ),
    path('message_view/', message_view, name = 'message_view'),
    path('reply_message/<int:message_id>/', reply_message, name = 'reply_message'),
    path('events/', events, name = 'events'),
    path('join_event/', join_event, name = 'join_event'),
    path('payments_page/', payment_page, name='payments_page'),
    path('process_payment/', process_payment, name='process_payment'),
    path('otp-verification/', otp_verification, name='otp_verification'),
    path('success_page/', process_payment, name = 'success_page'),
    path('generate_invoice/', generate_invoice, name= 'generate_invoice'),
    path('resources/', resources, name = 'resources'),
    path('book_appointment/', book_appointment, name = 'book_appointment'),
    path('emergencysupport/', EmergencySupport, name = 'emergencysupport'),
    path('discussion-group/', show_group, name = 'show_group'),
    path('books/', books_page, name='books'),
    path('podcasts/', podcasts_page, name='podcasts'),
    path('articles/', articles_page, name='articles'),
    path('upcoming-events/', upcoming_events, name='upcoming_events'),
    path('seminars/', seminars, name='seminars'),
    path('workshops/', workshops, name='workshops'),
    path('feedback/', feedback_view, name='feedback'),
    path('success/<int:feedback_id>/', feedback_success, name='feedback_success'),
    path('chatbot/', include('chatbot.urls')),
    path('policy/', policy, name = 'policy') ]



urlpatterns = urlpatterns+static(settings.MEDIA_URL,
                                 document_root=settings.MEDIA_ROOT)
