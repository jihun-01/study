import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { HeaderProvider } from './contexts/HeaderContext';

import './App.css';
import Header from './components/common/header/header';
import Footer from './components/common/footer/footer';
import Home from './components/page/home/home';
import StoreHome from './components/page/store/store';


function App() {
  

  return (
    <>
      <Header />
      <Router>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/store" element={<StoreHome />} />
          </Routes>
      </Router>
      <Footer />
    </>
  );
}

export default App;
