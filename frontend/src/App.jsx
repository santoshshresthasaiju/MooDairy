import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar';
import Homecard from './components/Homecard';

function App() {
  const [count, setCount] = useState(0);

  return (
    <Router>
      <Navbar />
      <Homecard/>
      <Routes>
        {/* Define your routes here */}
        {/* Example: */}
        {/* <Route path="/" element={<Home />} /> */}
        {/* <Route path="/about" element={<About />} /> */}
      </Routes>
    </Router>
  );
}

export default App;
