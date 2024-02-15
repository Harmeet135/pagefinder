import React, { useState, useEffect } from 'react';
import PdfData from './components/display';
import './App.css'
import './index.css';

const App = () => {
  const [isAva,setIsAva] = useState(false);
  return (
    <>
    <h1 className='heading'>Chat Bot</h1>
    <div className='main-container'>
    <PdfData  />
      <div>
        <h3>Ask Question</h3>
        </div>
        </div>
    </>
  );
};


export default App;