# chatbot/models.py
from django.db import models

class ChatSession(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('am', 'Amharic'),
        ('om', 'Afan Oromo'),
    ]
    
    ACCOUNT_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('joint', 'Joint'),
        ('company', 'Company'),
    ]
    
    session_id = models.CharField(max_length=255, unique=True)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='en')
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ConversationHistory(models.Model):
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='conversations')
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class RegisteredPhone(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)