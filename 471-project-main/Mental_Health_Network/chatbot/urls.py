from django.urls import path
from .views import *

urlpatterns = [
    path('', call_chatbot, name='call_chatbot'),
    path('chat/', chat_response, name='chat_response'),  # Adjusted to match your JS fetch call
]