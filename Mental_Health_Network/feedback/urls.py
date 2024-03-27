from django.urls import path
from feedback.views import *

urlpatterns = [
    path('', feedback_view, name='feedback'),
    path('success/<int:feedback_id>/', feedback_success, name='feedback_success'),
]