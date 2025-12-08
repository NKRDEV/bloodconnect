import React from 'react';
import Navbar from '@/components/Navbar';

export default function Dashboard() {
  return (
    <div>
      <Navbar />
      <main className="max-w-7xl mx-auto px-4 py-12">
        <h1 className="text-3xl font-bold text-gray-800 mb-6">Dashboard</h1>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-xl font-semibold text-gray-800 mb-2">Total Donors</h2>
            <p className="text-3xl font-bold text-red-600">0</p>
          </div>
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-xl font-semibold text-gray-800 mb-2">Blood Requests</h2>
            <p className="text-3xl font-bold text-red-600">0</p>
          </div>
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-xl font-semibold text-gray-800 mb-2">Completed Donations</h2>
            <p className="text-3xl font-bold text-red-600">0</p>
          </div>
        </div>
      </main>
    </div>
  );
}
