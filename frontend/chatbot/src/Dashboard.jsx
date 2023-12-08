import React, { useState } from 'react'
import Fab from './Fab'

export default function Dashboard() {
  const [completedProjectsOpen,setCompletedProjects] = useState(false);
  return (
    <div className='dashboard-container'>
      <div className="upper-dashboard">
        <div className="boxes"></div>
        <div className="boxes"></div>
        <div className="boxes"></div>
      </div>
      <div className="lower-dashboard">
        <h2>Projects</h2>
        <button className="project-section-tiles">
          Active Projects
          <img src="down-arrow.svg" alt="" width="10px" />
        </button>
        <button className="project-section-tiles">
          Upcoming Projects
          <img src="down-arrow.svg" alt="" width="10px" />
        </button>
        <button className="project-section-tiles">
          Recommended Projects
          <img src="down-arrow.svg" alt="" width="10px" />
        </button>
        <button onClick={()=>{setCompletedProjects(!completedProjectsOpen)}} className="project-section-tiles">
          Completed Projects
            {
              completedProjectsOpen?
              <img src="down-arrow.svg" alt="" width="10px" />
              :
              <img src="up-arrow.svg" alt="" width="10px" />
            }
        </button>
        <button className="project-section-tiles">
          Upcoming Payments
          <img src="down-arrow.svg" alt="" width="10px" />
        </button>
        <h2>Teams</h2>
        <button className="project-section-tiles">
          My Teams
          <img src="down-arrow.svg" alt="" width="10px" />
        </button>
        <button className="project-section-tiles">
          Team Invites
          <img src="down-arrow.svg" alt="" width="10px" />
        </button>
        <button className="project-section-tiles">
          Recommended Teams
          <img src="down-arrow.svg" alt="" width="10px" />
        </button>
        
      </div>
      <Fab/>
    </div>
  )
}