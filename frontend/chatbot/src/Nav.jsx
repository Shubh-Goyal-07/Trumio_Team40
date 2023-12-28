import React from 'react'
import { Link } from 'react-router-dom';

export default function Nav(){
  return (
    <div className='nav'>
        <img className="logo" src='trumio.png'></img>
        <div className="v-text">
            v0.0.11
        </div>
        
        <Link to="/dashboard" className='nav_text_btn'> Dashboard </Link>
        <Link to="/ehub" className='nav_text_btn'> EHub </Link>
        <Link to="" className='nav_text_btn'> Marketplace </Link>
        <Link to="/projects" className='nav_text_btn'> Project </Link>
        <Link to="" className='nav_text_btn'> My Team </Link>
        <Link to="" className='nav_text_btn'> Clubs </Link>
        
        <div className="nav-spacer"></div>

        <Link to="" className='nav_icon'> <img src="nav_icons/search.svg" alt="" width="20px" height="20px" /> </Link>
        <Link to="" className='nav_icon'> <img src="nav_icons/bell.svg" alt="" width="20px" height="20px" /> </Link>
        <Link to="/chat" className='nav_icon'> <img src="nav_icons/chat.svg" alt="" width="20px" height="20px" /> </Link>
    </div>
  )
}