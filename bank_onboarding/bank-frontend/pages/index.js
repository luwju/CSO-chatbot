// pages/index.js
import { useChat } from '../contexts/ChatContext';
import ChatInterface from '../components/ChatInterface';
import LanguageSelector from '../components/LanguageSelector';

export default function Home() {
  const { currentStep } = useChat();

  return (
    <main className="h-screen">
      {currentStep === 'language' ? <LanguageSelector /> : <ChatInterface />}
    </main>
  );
}