import React from 'react'

export default function Nav({changeTab}){
  return (
    <div className='nav'>
        <img className="logo" src='trumio.png'></img>
        <div className="v-text">
            v0.0.11
        </div>
        <button onClick={()=>changeTab(true)}>
            Dashboard
        </button>
        <button>
            Marketplace
        </button>
        <button>
            Project
        </button>
        <button>
            My Team
        </button>
        <button onClick={()=>changeTab(false)}>
            Chats
        </button>
        <button className='right-icons'>
            <img src="" alt="" />
        </button>
    </div>
  )
}