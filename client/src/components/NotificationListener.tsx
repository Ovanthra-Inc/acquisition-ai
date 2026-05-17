'use client';

import { useEffect } from 'react';
import { toast } from 'sonner';

export default function NotificationListener() {
  useEffect(() => {
    // In a real app, get user_id from auth context
    const userId = "test-user-id"; 
    const wsUrl = `ws://localhost:8000/ws/${userId}`;
    
    let socket: WebSocket | null = null;
    let reconnectTimeout: NodeJS.Timeout;

    const connect = () => {
      console.log('Connecting to WebSocket:', wsUrl);
      socket = new WebSocket(wsUrl);

      socket.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          console.log('Notification received:', data);
          
          toast(data.title || 'New Notification', {
            description: data.message || data.content || 'You have a new update.',
            action: {
              label: 'View',
              onClick: () => console.log('View clicked'),
            },
          });
        } catch (err) {
          console.error('Failed to parse WebSocket message:', err);
        }
      };

      socket.onclose = () => {
        console.log('WebSocket disconnected. Retrying in 5s...');
        reconnectTimeout = setTimeout(connect, 5000);
      };

      socket.onerror = (err) => {
        console.error('WebSocket error:', err);
        socket?.close();
      };
    };

    connect();

    return () => {
      if (socket) {
        socket.onclose = null;
        socket.close();
      }
      clearTimeout(reconnectTimeout);
    };
  }, []);

  return null; // This component doesn't render anything
}
