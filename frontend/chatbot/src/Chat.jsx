import React, { useState } from 'react'
import Nav from './Nav'
import './App.css'
import axios from 'axios'

export default function Chat() {
  const [projectChats,setProjectChats] = useState(true);
  const [selectedProject,setSelectedProject] = useState("Trumio");
  const [inputText, setInputText] = useState("");
  const userName = "Asharma538";

  const handleSelectedProject = (project) => {
    document.getElementById('chats').innerHTML = "";
    setSelectedProject(project);
  }

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  const handleProjectVisibility = () => {
    setProjectChats(!projectChats);
  }
  
  const handleQuestion = async() => {

    console.log(selectedProject);
    setInputText('');
    var chatDiv = document.getElementById('chats');
    var newChat = document.createElement("div");
    newChat.classList.add('chat');
    newChat.innerHTML="<div class=\"name\">"+userName+"</div>";
    newChat.innerHTML+="<div class=\"message-text\">"+inputText+"</div>";
    chatDiv.appendChild(newChat);
    axios({
      method: 'POST',
      url: 'http://127.0.0.1:8000/chat/',
      data: {
        project_id: selectedProject,
        user_id: userName,
        question: inputText
      }
    })
    .then((response) => {
      console.log(response);
      var res = response.data.message;
      var newResponse = document.createElement("div");
      newResponse.classList.add('chat');
      newResponse.innerHTML="<div class=\"name_c\">"+"AI Chatbot"+"</div>";
      newResponse.innerHTML+="<div class=\"message-text\">"+res+"</div>";
      chatDiv.appendChild(newResponse);
    });

    // inputText gives the question,
    // selectedProject gives the project_id
  }

  return (
    <div>
      <main className='main-container'>
        <div className='chat-selection-container'>
          <div className="search-section">
            <img className='prof-pic' src="vite.svg" alt="" />
            <div className="search-bar">
              <img src="search.png" alt="" width="15px" height="15px" />
              Search or start a new chat
            </div>
          </div>
          <div className="direct-chat-section">
            <img src="up_arrow.png" alt="" width="23px" height="23px" /> <div className="chat-cat-text">Direct Chat</div> <img src="add.png" alt="" width="20px" height="20px" />
          </div>
          <div className="project-chat-section">
            <img src="up_arrow.png" alt="" width="23px" height="23px" /> <div className="chat-cat-text">Project Chat</div>
          </div>
          <div className="group-chat-section">
            <img src="up_arrow.png" alt="" width="23px" height="23px" /> <div className="chat-cat-text">Group Chat</div> <img src="add.png" alt="" width="20px" height="20px" />
          </div>
          {
            projectChats?
            <>
              <button className="project-chat-section" onClick={handleProjectVisibility}>
                <img src="down_arrow.png" alt="" width="23px" height="23px" /> <div className="chat-cat-text">Project Chatbots</div>
              </button>
              
              <button className='project-tile' onClick={()=>handleSelectedProject("Trumio")}>
                <div className='project-icon'>T</div>
                <p className='project-name'>Trumio</p>
              </button>

              <button className='project-tile' onClick={()=>handleSelectedProject("DevRev")}>
                <div className='project-icon'>D</div>
                <p className='project-name'>Devrev</p>
              </button>

            </>
            :
            <button className="project-chat-section" onClick={handleProjectVisibility}>
              <img src="up_arrow.png" alt="" width="23px" height="23px" /> <div className="chat-cat-text">Project Chatbots</div>
            </button>
          }
        </div>
        <div className="chat-container">
          <div className="chatbot-desc">
            <img src="chatbot.png" alt="" width="45px" />
            <div className="name">
              AI Chatbot
            </div>
          </div>
          <div className="chats" id='chats'>
            
          </div>
          <div className="message-area">
            <input type="text" placeholder="Type your message..." value={inputText} onChange={handleInputChange} className='question'/>
            <button type="submit" className='question-send' value="Send" placeholder="Enter your message here" onClick={handleQuestion}>Send</button>
          </div>
        </div>
      </main>
    </div>
  )
}