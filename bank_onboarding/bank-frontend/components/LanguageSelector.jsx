// components/LanguageSelector.js
import { useChat } from '@/contexts/ChatContext';
import { initializeChat } from '@/lib/api';


export default function LanguageSelector() {
  const { setLanguage, setSessionId, setCurrentStep, addMessage, setIsLoading } = useChat();

  const languages = [
    { code: 'en', name: 'English', native: 'English' },
    { code: 'am', name: 'Amharic', native: 'አማርኛ' },
    { code: 'om', name: 'Afan Oromo', native: 'Afaan Oromoo' }
  ];

  const handleLanguageSelect = async (langCode) => {
    setIsLoading(true);
    setLanguage(langCode);
    
    try {
      const response = await initializeChat(langCode);
      setSessionId(response.session_id);
      setCurrentStep('main');
      
      const welcomeMessages = {
        en: "Welcome! You've selected English. Please choose your account type by typing: Individual, Joint, or Company.",
        am: "እንኳን ደህና መጡ! አማርኛ መርጠዋል። እባክዎ የመለያ አይነትዎን በመጻፍ ይምረጡ: ግለሰብ, ሁለት ወይም ከዚያ በላይ, ወይም ኩባንያ።",
        om: "Baga nagaan dhuftan! Afaan Oromoo filatte. Maaloo gara'umsa herregaa barreessuun filadhu: Nama tokko, Walitti qabdu, ykn Kampanii."
      };
      
      addMessage(welcomeMessages[langCode], false);
    } catch (error) {
      addMessage('Sorry, failed to initialize chat. Please try again.', false);
      console.error('Language selection error:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-xl p-8 max-w-md w-full">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-800 mb-2">🏦</h1>
          <h2 className="text-2xl font-bold text-gray-800 mb-2">
            Welcome to Our Bank
          </h2>
          <p className="text-gray-600">
            Please select your preferred language
          </p>
        </div>
        
        <div className="space-y-4">
          {languages.map((lang) => (
            <button
              key={lang.code}
              onClick={() => handleLanguageSelect(lang.code)}
              className="w-full p-4 border-2 border-gray-200 rounded-lg hover:border-blue-500 hover:bg-blue-50 transition-all duration-200 text-left"
            >
              <div className="font-semibold text-gray-800 text-lg">{lang.name}</div>
              <div className="text-sm text-gray-600">{lang.native}</div>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
