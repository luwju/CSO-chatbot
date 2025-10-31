// lib/api.js
const API_BASE_URL = 'http://localhost:8000/api';

export const initializeChat = async (language) => {
  try {
    const response = await fetch(`${API_BASE_URL}/chat/init/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ language }),
    });
    
    if (!response.ok) {
      throw new Error('Failed to initialize chat');
    }
    
    return await response.json();
  } catch (error) {
    console.error('API Error - init:', error);
    throw error;
  }
};

export const sendMessage = async (sessionId, message, language) => {
  try {
    const response = await fetch(`${API_BASE_URL}/chat/message/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        session_id: sessionId,
        message: message,
        language: language
      }),
    });
    
    if (!response.ok) {
      throw new Error('Failed to send message');
    }
    
    return await response.json();
  } catch (error) {
    console.error('API Error - message:', error);
    throw error;
  }
};