import { useEffect } from 'react'
import React from 'react'
import Fab from './Fab'

export default function Dashboard() {
  useEffect(()=>{
    document.addEventListener('DOMContentLoaded', function () {
      var floatingButton = document.querySelector('.floatingButton');
      var floatingMenu = document.querySelector('.floatingMenu');
      var floatingButtonWrap = document.querySelector('.floatingButtonWrap');
  
      floatingButton.addEventListener('click', function (e) {
          e.preventDefault();
          this.classList.toggle('open');
          
          var icon = this.querySelector('.fa');
          if (icon.classList.contains('fa-plus')) {
              icon.classList.remove('fa-plus');
              icon.classList.add('fa-close');
          } else if (icon.classList.contains('fa-close')) {
              icon.classList.remove('fa-close');
              icon.classList.add('fa-plus');
          }
  
          floatingMenu.style.display = (floatingMenu.style.display === 'none' || floatingMenu.style.display === '') ? 'block' : 'none';
      });
  
      document.addEventListener('click', function (e) {
          var container = document.querySelector('.floatingButton');
  
          if (!(container === e.target || container.contains(e.target)) && floatingButtonWrap.contains(e.target) === false) {
              if (container.classList.contains('open')) {
                  container.classList.remove('open');
              }
  
              var icon = container.querySelector('.fa');
              if (icon.classList.contains('fa-close')) {
                  icon.classList.remove('fa-close');
                  icon.classList.add('fa-plus');
              }
  
              floatingMenu.style.display = 'none';
          }
  
          if (!(container === e.target) && floatingMenu.contains(e.target)) {
              floatingButton.classList.remove('open');
              floatingMenu.style.display = (floatingMenu.style.display === 'none' || floatingMenu.style.display === '') ? 'block' : 'none';
          }
      });
  });
  
  },[]);
  return (
    <div className='dashboard-container'>
      <img src="bg-dashboard.png" alt="" width="100%" />
      <Fab/>
    </div>
  )
}