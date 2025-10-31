# api/serializers.py
from rest_framework import serializers
from chatbot.models import ChatSession, ConversationHistory

class ChatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSession
        fields = ['session_id', 'language', 'account_type', 'phone_number', 'is_verified']

class ConversationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationHistory
        fields = ['user_message', 'bot_response', 'timestamp']

class MessageSerializer(serializers.Serializer):
    session_id = serializers.CharField(required=False)
    message = serializers.CharField()
    language = serializers.CharField(default='en')

class PhoneVerificationSerializer(serializers.Serializer):
    session_id = serializers.CharField()
    phone_number = serializers.CharField()

class OTPVerificationSerializer(serializers.Serializer):
    session_id = serializers.CharField()
    otp = serializers.CharField()