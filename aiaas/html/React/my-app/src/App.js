import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';

import './App.css';
import Header from './components/common/header';
import Footer from './components/common/footer';
import MainPage from './components/page/mainpage';
import StoreHome from './components/page/store/store';
function App() {
  

  return (
    <>
    <Header />
    <Router>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/store" element={<StoreHome />} />
      </Routes>
    </Router>
    <Footer />
    </>
  );
}

export default App;
