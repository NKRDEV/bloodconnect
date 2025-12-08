import React from 'react';

interface NavbarProps {}

export default function Navbar({}: NavbarProps) {
  return (
    <nav className="bg-red-600 text-white shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center">
            <h1 className="text-2xl font-bold">BloodConnect</h1>
          </div>
          <div className="flex gap-6">
            <a href="/" className="hover:text-red-200">
              Home
            </a>
            <a href="/dashboard" className="hover:text-red-200">
              Dashboard
            </a>
            <a href="/about" className="hover:text-red-200">
              About
            </a>
          </div>
        </div>
      </div>
    </nav>
  );
}
