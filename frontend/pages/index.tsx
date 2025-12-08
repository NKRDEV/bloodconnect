import React, { useEffect, useState } from 'react';
import Navbar from '@/components/Navbar';
import apiClient from '@/utils/api';

export default function Home() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await apiClient.get('/health');
        setMessage(`Backend is running: ${response.data.message}`);
      } catch (error) {
        setMessage('Unable to connect to backend');
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <Navbar />
      <main className="max-w-7xl mx-auto px-4 py-12">
        <div className="text-center">
          <h1 className="text-4xl font-bold text-red-600 mb-4">Welcome to BloodConnect</h1>
          <p className="text-xl text-gray-600 mb-8">
            Connecting blood donors with those in need
          </p>
          <div className="bg-white rounded-lg shadow p-6">
            <p className="text-lg text-gray-700">{message}</p>
          </div>
        </div>
      </main>
    </div>
  );
}
