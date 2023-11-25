import React from 'react'

export default function Nav() {
  return (
    <div className='nav'>
        <img className="logo" src='trumio.png'></img>
        <div className="v-text">
            v0.0.11
        </div>
        <button>
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
        <button className='right-icons'>
            <img src="" alt="" />
        </button>
    </div>
  )
}