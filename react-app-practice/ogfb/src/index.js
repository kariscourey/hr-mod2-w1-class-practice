import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const numbers = [1,2,3,4,5]
const colors = ['red', 'orange']
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App numbers={numbers} colors={colors}/>
  </React.StrictMode>
);
