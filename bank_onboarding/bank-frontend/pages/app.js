// pages/_app.js
import { ChatProvider } from '@/contexts/ChatContext';
import '@/styles/globals.css';

export default function App({ Component, pageProps }) {
  return (
    <ChatProvider>
      <Component {...pageProps} />
    </ChatProvider>
  );
}
