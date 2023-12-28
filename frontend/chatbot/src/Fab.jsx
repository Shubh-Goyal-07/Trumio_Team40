import React, { useEffect, useState } from 'react'
import axios from 'axios';

export default function Fab() {
    const [clicked,setClicked] = useState(false);
    const [inputText, setInputText] = useState("");
    const userName = "Asharma538";
    const projectId = "Trumio"

    const handleClick = () => {
        setClicked(!clicked);
    }
    const handleInputChange = (e) => {
        setInputText(e.target.value);
    };
    const handleQuestionSubmit = () => {
        var chatDiv = document.getElementById('fab-chats');
        var newChat = document.createElement("div");
        newChat.classList.add('fab-chat');
        newChat.innerHTML += "<div class=\"name\">"+userName+"</div>"
        newChat.innerHTML += "<div class=\"message-text\">"+inputText+"</div>"
        chatDiv.appendChild(newChat);
        console.log(inputText,userName,projectId);
        axios({
            method: 'POST',
            url: 'http://127.0.0.1:8000/chat/',
            data: {
              project_id: projectId,
              user_id: userName,
              question: inputText
            }
          })
          .then((response) => {
            console.log(response);
            var res = response.data.message;
            var newResponse = document.createElement("div");
            newResponse.classList.add('fab-chat');
            newResponse.innerHTML="<div class=\"name_c\">AI Chatbot</div>";
            newResponse.innerHTML+="<div class=\"message-text\">"+res+"</div>";
            chatDiv.appendChild(newResponse);
          });
      
        
    }

    if (!clicked)
        return (
            <button onClick={handleClick} className='fab-button'>
                <div className='fab'>
                    <img src="msg.avif" alt="" srcset="" width="100px" height="100px" />
                </div>
            </button>
        );
    else
        return (
            <>
            <div className='fab-chat-section'>
                <div className="fab-chat-proj">
                    <img src="chatbot.png" alt="" width="40px" height="40px" />
                    <div className="proj-title">Trumio</div>
                </div>
                <div className='fab-chats' id='fab-chats'>

                </div>
                <input type="text" onChange={handleInputChange} value={inputText} className='fab-question' placeholder='Write your question here...' />
                <button className='fab-submit' onClick={handleQuestionSubmit}>Submit</button>
            </div>
            <button onClick={handleClick}>
                <div className='fab cross'>
                    &#10005;
                </div>
            </button>
            </>
        );
        
}