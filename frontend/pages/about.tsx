import React from 'react';
import Navbar from '@/components/Navbar';

export default function About() {
  return (
    <div>
      <Navbar />
      <main className="max-w-7xl mx-auto px-4 py-12">
        <h1 className="text-3xl font-bold text-gray-800 mb-6">About BloodConnect</h1>
        <div className="bg-white rounded-lg shadow p-8">
          <p className="text-lg text-gray-700 mb-4">
            BloodConnect is a platform dedicated to connecting blood donors with those in need.
          </p>
          <p className="text-lg text-gray-700 mb-4">
            Our mission is to make blood donation accessible and convenient for everyone.
          </p>
          <p className="text-lg text-gray-700">
            Join us in making a difference in someone's life.
          </p>
        </div>
      </main>
    </div>
  );
}
