import React, { useState } from 'react';
import { Link } from 'react-router-dom'; // If using React Router
import logo from "../assets/mooologo.png"

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <nav className="bg-cyan-600 max-w-1280px px-8 md:px-16 lg:px-24 xl:px-48">
      <div className="container mx-auto px-4 py-4 flex justify-between items-center">
        <Link to="/" className="text-white font-bold text-lg">
          <img 
            alt="Simple Dairy" 
            loading="lazy" 
            width="123" 
            height="75" 
            decoding="async" 
            style={{ color: 'transparent' }} 
            src={logo}
          />
        </Link>
        <button 
          type="button" 
          aria-label="Toggle navigation" 
          className="text-white focus:outline-none md:hidden" 
          onClick={toggleMenu}
        >
          <svg 
            className="w-6 h-6" 
            fill="none" 
            stroke="currentColor" 
            viewBox="0 0 24 24" 
            xmlns="http://www.w3.org/2000/svg"
          >
            <path 
              strokeLinecap="round" 
              strokeLinejoin="round" 
              strokeWidth="2" 
              d="M4 6h16M4 12h16m-7 6h7" 
            />
          </svg>
        </button>
        <div className={`md:flex md:items-center md:space-x-6 ${isOpen ? 'block' : 'hidden'}`}>
          <div className="flex flex-col md:flex-row md:space-x-6 text-white">
            <Link to="/" className="py-2 md:py-0">Home</Link>
            <Link to="/about" className="py-2 md:py-0">About</Link>
            <Link to="/services" className="py-2 md:py-0">Services</Link>
            <Link to="/features" className="py-2 md:py-0">Features</Link>
            <Link to="/pricing" className="py-2 md:py-0">Pricing</Link>
            <Link to="/contact" className="py-2 md:py-0">Contact</Link>
            <Link to="/login" className="py-2 md:py-0">Login</Link>
            <Link to="/signup" className="py-2 md:py-0">Create an Account</Link>
            <Link to="/dashboard" className="py-2 md:py-0">Dashboard</Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
