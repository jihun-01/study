import './App.css';
import Header from './components/Header/Header';
import OutboundQR from './components/page/OutboundQR';
import OutboundOCR from './components/page/OutboundOCR';
import OutboundResult from './components/page/OutboundResult';
import {Routes, Route, BrowserRouter as Router } from 'react-router-dom';
import WmsApp from './WmsApp';

function App() {
  return (
    <>
      <Router>
        <Header />
        <Routes>
          <Route path="/" element={<OutboundQR />} />
          <Route path="/ocr" element={<OutboundOCR />} />
          <Route path="/result" element={<OutboundResult />} />
        </Routes>
        <WmsApp />
      </Router>
    </>
  );
}

export default App;
