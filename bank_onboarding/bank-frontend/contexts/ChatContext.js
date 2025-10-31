// contexts/ChatContext.js
import { createContext, useContext, useState } from 'react';

const ChatContext = createContext();

export function ChatProvider({ children }) {
  const [messages, setMessages] = useState([]);
  const [sessionId, setSessionId] = useState(null);
  const [language, setLanguage] = useState('en');
  const [accountType, setAccountType] = useState(null);
  const [currentStep, setCurrentStep] = useState('language');
  const [isWaitingForOTP, setIsWaitingForOTP] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const addMessage = (text, isUser = false) => {
    setMessages(prev => [...prev, { 
      id: Date.now() + Math.random(), 
      text, 
      isUser, 
      timestamp: new Date() 
    }]);
  };

  const resetChat = () => {
    setMessages([]);
    setSessionId(null);
    setAccountType(null);
    setCurrentStep('language');
    setIsWaitingForOTP(false);
  };

  return (
    <ChatContext.Provider value={{
      messages,
      sessionId,
      language,
      accountType,
      currentStep,
      isWaitingForOTP,
      isLoading,
      setSessionId,
      setLanguage,
      setAccountType,
      setCurrentStep,
      setIsWaitingForOTP,
      setIsLoading,
      addMessage,
      resetChat
    }}>
      {children}
    </ChatContext.Provider>
  );
}

export const useChat = () => {
  const context = useContext(ChatContext);
  if (!context) {
    throw new Error('useChat must be used within a ChatProvider');
  }
  return context;
};