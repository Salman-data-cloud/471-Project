from django.urls import path
from . import views
urlpatterns = [
    path('send-email/', views.send_email_view, name='send_email'),
    path('', views.profile, name = 'profile'),
    path('email-sent/', views.email_sent_view, name='email_sent'),
    path('write-blog/', views.blog_writing_view, name='blog_writing_page'),
    path('doctor-white/', views.doctor_white_view, name='doctor_white_page')
]