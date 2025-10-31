# chatbot/responses.py
RESPONSES = {
    'en': {
        'welcome': "Welcome! Please choose your preferred language: English, Afan Oromo, or Amharic.",
        'language_set': "Great! You've selected English. Please choose your account type: Individual, Joint, or Company.",
        'account_type_selected': "Thank you for selecting {account_type}. How can I help you?",
        'ask_documents_individual': "For an Individual account, you'll need:\n• Valid government-issued ID\n• Proof of address (utility bill)\n• Recent passport photo\n• Initial deposit amount",
        'ask_documents_joint': "For a Joint account, you'll need:\n• IDs for all account holders\n• Proof of address for primary holder\n• Partnership agreement (if applicable)\n• All holders must be present",
        'ask_documents_company': "For a Company account, you'll need:\n• Company registration certificate\n• Memorandum & Articles of Association\n• Board resolution for account opening\n• IDs of all directors\n• Company tax certificate",
        'branch_info': "We have branches in:\n• Addis Ababa - Bole\n• Addis Ababa - Mexico\n• Addis Ababa - Piazza\n• Dire Dawa\n• Hawassa\nWhich location are you interested in?",
        'contact_cso': "To contact a Customer Service Officer, please provide your phone number for OTP verification.",
        'enter_phone': "Please enter your 10-digit phone number:",
        'invalid_phone': "Please enter a valid 10-digit phone number.",
        'phone_already_registered': "This phone number is already registered. Please use a different number.",
        'otp_sent': "OTP has been sent to your phone. Please enter the OTP (use 2333 for demo):",
        'invalid_otp': "Invalid OTP. Please try again.",
        'otp_verified': "OTP verified successfully! A Customer Service Officer will contact you shortly.",
        'fallback': "I'm not sure I understand. You can ask about:\n• Account types\n• Document requirements\n• Branch information\n• Contacting a CSO",
    },
    'am': {
        'welcome': "እንኳን ደህና መጡ! እባክዎ የተመረጠልዎትን ቋንቋ ይምረጡ: English, Afan Oromo, or Amharic.",
        'language_set': "ጥሩ! አማርኛ መርጠዋል። እባክዎ የመለያ አይነትዎን ይምረጡ: ግለሰብ, ሁለት ወይም ከዚያ በላይ, ወይም ኩባንያ።",
        # ... Add all Amharic translations
    },
    'om': {
        'welcome': "Baga nagaan dhuftan! Maaloo afaan filadhu: English, Afan Oromo, or Amharic.",
        'language_set': "Gaari! Afaan Oromoo filatte. Maaloo gara'umsa herregaa filadhu: Nama tokko, Walitti qabdu, ykn Kampanii.",
        # ... Add all Afan Oromo translations
    }
}

DOCUMENT_REQUIREMENTS = {
    'individual': ['valid_id', 'proof_of_address', 'passport_photo', 'initial_deposit'],
    'joint': ['ids_all_holders', 'proof_of_address_primary', 'partnership_agreement', 'all_holders_present'],
    'company': ['registration_certificate', 'memorandum_articles', 'board_resolution', 'directors_ids', 'tax_certificate']
}