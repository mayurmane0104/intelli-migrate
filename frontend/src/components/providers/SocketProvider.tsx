'use client';

import React, { createContext, useContext, useEffect, useState } from 'react';
import { io, type Socket } from 'socket.io-client';

interface SocketContextType {
    socket: Socket | null;
    connected: boolean;
}

const SocketContext = createContext<SocketContextType>({ socket: null, connected: false });

export const useSocket = () => useContext(SocketContext);

export const SocketProvider = ({ children }: { children: React.ReactNode }) => {
    const [socket, setSocket] = useState<Socket | null>(null);
    const [connected, setConnected] = useState(false);

    useEffect(() => {
        // Connect to the Fastify backend server (configured via NEXT_PUBLIC_API_URL)
        const backendUrl =
            typeof window !== 'undefined'
                ? window.location.origin
                : (process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3001');
        const isDev = process.env.NODE_ENV !== 'production';
        const socketInstance = io(backendUrl, {
            transports: ['websocket'],
            reconnection: !isDev,
            reconnectionAttempts: isDev ? 0 : 5,
            timeout: 8000,
            autoConnect: true,
        });

        const onConnect = () => setConnected(true);
        const onDisconnect = () => setConnected(false);

        socketInstance.on('connect', onConnect);
        socketInstance.on('disconnect', onDisconnect);

        setSocket(socketInstance);

        return () => {
            socketInstance.off('connect', onConnect);
            socketInstance.off('disconnect', onDisconnect);
            socketInstance.removeAllListeners();
            socketInstance.disconnect();
            setSocket(null);
            setConnected(false);
        };
    }, []);

    return (
        <SocketContext.Provider value={{ socket, connected }}>
            {children}
        </SocketContext.Provider>
    );
};
