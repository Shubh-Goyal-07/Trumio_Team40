import React, { useState } from 'react'
import Chat from './Chat'
import Nav from './Nav';
import './App.css'
import Dashboard from './Dashboard';
import Project from './Project';

export default function App() {
  const [tab,setTab] = useState(false);
  const handleTabChange = (status) => {
    setTab(status);
  }
  return(
    <div>
      <Nav changeTab={handleTabChange}/>  
      {
        tab?
        <Dashboard/>
        :
        <Chat/>
      }
    </div>
  )
}