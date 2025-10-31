# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chat/init/', views.init_chat, name='init_chat'),
    path('chat/message/', views.chat_message, name='chat_message'),
    path('verify-phone/', views.verify_phone, name='verify_phone'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
]