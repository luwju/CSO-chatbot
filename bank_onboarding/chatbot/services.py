# chatbot/services.py
from fuzzywuzzy import fuzz
import uuid
from django.core.validators import validate_integer
from django.core.exceptions import ValidationError
from .models import ChatSession, ConversationHistory, RegisteredPhone
from .responses import RESPONSES, DOCUMENT_REQUIREMENTS

class ChatbotEngine:
    def __init__(self):
        self.intents = [
            'select_individual', 'select_joint', 'select_company',
            'ask_documents', 'find_branch', 'contact_cso', 
            'greeting', 'help', 'unknown'
        ]
    
    def detect_intent(self, user_input, language='en'):
        """Use fuzzy matching to detect user intent"""
        user_input = user_input.lower().strip()
        
        # Intent patterns for different languages
        intent_patterns = {
            'select_individual': ['individual', 'single', 'personal', 'one person'],
            'select_joint': ['joint', 'two', 'multiple', 'together', 'partnership'],
            'select_company': ['company', 'business', 'corporate', 'organization'],
            'ask_documents': ['document', 'require', 'need', 'paper', 'what do i need'],
            'find_branch': ['branch', 'location', 'where', 'office', 'near me'],
            'contact_cso': ['contact', 'speak', 'talk to', 'officer', 'human', 'person'],
            'greeting': ['hello', 'hi', 'hey', 'good morning', 'good afternoon'],
            'help': ['help', 'what can you do', 'options', 'menu']
        }
        
        best_intent = 'unknown'
        best_score = 0
        
        for intent, patterns in intent_patterns.items():
            for pattern in patterns:
                score = fuzz.partial_ratio(user_input, pattern)
                if score > best_score and score > 60:  # Threshold
                    best_score = score
                    best_intent = intent
        
        return best_intent
    
    def generate_response(self, intent, session, user_input=None):
        """Generate appropriate response based on intent and session context"""
        language = session.language
        
        if intent == 'greeting':
            return RESPONSES[language]['welcome']
        
        elif intent in ['select_individual', 'select_joint', 'select_company']:
            account_type = intent.replace('select_', '')
            session.account_type = account_type
            session.save()
            return RESPONSES[language]['account_type_selected'].format(account_type=account_type.capitalize())
        
        elif intent == 'ask_documents':
            if not session.account_type:
                return RESPONSES[language]['fallback']
            return RESPONSES[language][f'ask_documents_{session.account_type}']
        
        elif intent == 'find_branch':
            return RESPONSES[language]['branch_info']
        
        elif intent == 'contact_cso':
            return RESPONSES[language]['contact_cso']
        
        else:
            return RESPONSES[language]['fallback']
    
    def handle_phone_verification(self, phone_number, session):
        """Handle phone number validation and OTP process"""
        # Validate phone number format
        try:
            validate_integer(phone_number)
            if len(phone_number) != 10:
                return False, "invalid_phone"
        except (ValidationError, ValueError):
            return False, "invalid_phone"
        
        # Check if phone is already registered
        if RegisteredPhone.objects.filter(phone_number=phone_number).exists():
            return False, "phone_already_registered"
        
        session.phone_number = phone_number
        session.save()
        return True, "otp_sent"
    
    def verify_otp(self, otp_input, session):
        """Verify OTP (demo: 2333)"""
        if otp_input == "2333":
            session.is_verified = True
            session.save()
            
            # Store the phone number as registered
            if session.phone_number:
                RegisteredPhone.objects.get_or_create(phone_number=session.phone_number)
            
            return True, "otp_verified"
        else:
            return False, "invalid_otp"

# Singleton instance
chatbot_engine = ChatbotEngine()