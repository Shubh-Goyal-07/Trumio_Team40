import React, { useState } from 'react'
import { Route, Routes, BrowserRouter } from 'react-router-dom';
import Nav from './Nav';
import './App.css'
import Dashboard from './Dashboard';
import Project from './Project';
import Chat from './Chat'
import EHub from './EHub';

export default function App() {
  
  return(
    <BrowserRouter>
      <Nav/>
      <Routes>
          <Route path="/" element={<Dashboard/>} />
          <Route path="/dashboard" element={<Dashboard/>} />
          <Route path="/ehub" element={<EHub/>} />
          <Route path="/chat" element={<Chat/>} />
          <Route path="/projects" element={<Project/>} />
      </Routes>
    </BrowserRouter>
  )
}