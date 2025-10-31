# api/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import uuid
from chatbot.models import ChatSession, ConversationHistory
from chatbot.services import chatbot_engine
from .serializers import *

@api_view(['POST'])
def init_chat(request):
    """Initialize a new chat session"""
    language = request.data.get('language', 'en')
    
    # Create new session
    session_id = str(uuid.uuid4())
    session = ChatSession.objects.create(
        session_id=session_id,
        language=language
    )
    
    # Store welcome message
    welcome_message = chatbot_engine.generate_response('greeting', session)
    ConversationHistory.objects.create(
        session=session,
        user_message="",
        bot_response=welcome_message
    )
    
    return Response({
        'session_id': session_id,
        'bot_response': welcome_message,
        'language': language
    })

@api_view(['POST'])
def chat_message(request):
    """Handle chat messages"""
    serializer = MessageSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    data = serializer.validated_data
    session_id = data.get('session_id')
    user_message = data['message']
    language = data['language']
    
    try:
        session = ChatSession.objects.get(session_id=session_id)
        session.language = language  # Update language if changed
        session.save()
    except ChatSession.DoesNotExist:
        return Response({'error': 'Invalid session'}, status=status.HTTP_404_NOT_FOUND)
    
    # Detect intent and generate response
    intent = chatbot_engine.detect_intent(user_message, language)
    bot_response = chatbot_engine.generate_response(intent, session, user_message)
    
    # Store conversation
    ConversationHistory.objects.create(
        session=session,
        user_message=user_message,
        bot_response=bot_response
    )
    
    return Response({
        'session_id': session_id,
        'bot_response': bot_response,
        'intent': intent
    })

@api_view(['POST'])
def verify_phone(request):
    """Verify phone number"""
    serializer = PhoneVerificationSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    data = serializer.validated_data
    session_id = data['session_id']
    phone_number = data['phone_number']
    
    try:
        session = ChatSession.objects.get(session_id=session_id)
    except ChatSession.DoesNotExist:
        return Response({'error': 'Invalid session'}, status=status.HTTP_404_NOT_FOUND)
    
    success, message_key = chatbot_engine.handle_phone_verification(phone_number, session)
    
    response_data = {
        'success': success,
        'message': chatbot_engine.RESPONSES[session.language][message_key]
    }
    
    if success:
        response_data['next_step'] = 'otp_verification'
    
    return Response(response_data)

@api_view(['POST'])
def verify_otp(request):
    """Verify OTP"""
    serializer = OTPVerificationSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    data = serializer.validated_data
    session_id = data['session_id']
    otp = data['otp']
    
    try:
        session = ChatSession.objects.get(session_id=session_id)
    except ChatSession.DoesNotExist:
        return Response({'error': 'Invalid session'}, status=status.HTTP_404_NOT_FOUND)
    
    success, message_key = chatbot_engine.verify_otp(otp, session)
    
    return Response({
        'success': success,
        'message': chatbot_engine.RESPONSES[session.language][message_key]
    })