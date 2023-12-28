import {Children, React,useState} from 'react'
import axios, { getAdapter } from 'axios'
const backendURL = "https://avatar.rohitkori.tech"
export default function EHub() {
  const [step, setStep] = useState(1);

  const reverseStep = () => {
    setStep(()=>step-1);
  }
  
  const [pointers,setPointers] = useState(""); // for storing pointers from client
  const handlePointersChange = (e) => {setPointers(e.target.value);}
  
  const [topic,setTopic] = useState(""); // for storing pointers from client
  const handleTopicChange = (e) => {setTopic(e.target.value);}
  
  const [content,setContent] = useState(''); // for storing the content generated from pointers
  const handleContentChange = (e) => {setContent(e.target.value);}

  const [avatar_links,setAvatarLinks] = useState(["avatars/avt1.jpeg","avatars/avt1.jpeg","avatars/avt1.jpeg"]);
  const [selectedAvatar,setSelectedAvatar] = useState("");

  const [videosrc,setVideosrc] = useState();
  
  const [file,setFile] = useState({file: null});


  const handleFileChange = (e) => {
    setSelectedAvatar("");
    setFile({ file: e.target.files[0] });
  }

  const getContentFromPointers = () =>{
    // content getter function will come here, content will be recieved in md format text, will be formatted later
    console.log(pointers,topic);
    const formData = new FormData();
    formData.append("user_id","Pranav");
    formData.append("topic","topic")
    formData.append("pointers",pointers)
      axios.post(backendURL+'/send-pointer',formData)
        .then((res)=>{
          console.log(res.data);
          setContent(res.data.content);
          handleStepChange();
        }
        ).catch((err)=>{
          console.log(err);
        });
      // setContent(pointers);
      // handleStepChange();
  }

  const getavatar = async() => {
    await axios.get(backendURL+"/get-avatar",{
     params: {
      user_id: "Pranav"
     } 
    }).then((res)=>{
      var img_urls = [];
      for(var i=0;i<res.data.data.length;i++){
        img_urls.push(res.data.data[i].image_url);
      }
      setAvatarLinks(img_urls);
    }).catch((err)=>{
      console.log(err);
    });
  }

  const handlesubmitContent = async() => {
    // user has submitted the content now we can use it for video
    await getavatar();
    handleStepChange();
  }

  const handleAvatarSelect = (idx) => {
    console.log(avatar_links[idx]);
    setSelectedAvatar(avatar_links[idx]);
  }


  const createAvatar = () => {
    const formdata = new FormData();
    formdata.append("user_id","Pranav")
    formdata.append("image_url",file.file)
    console.log(file.file);
    console.log("creating avt");
    axios.post(backendURL+'/create-image',
      formdata
    )
      .then(async (res)=>{
        await getavatar();
        setFile({file:null});
      }
      ).catch((err)=>{
        console.log("error");
        console.log(err);
      });
  }

  const getVideo = () => {
    const formData = new FormData();
    formData.append("user_id","Pranav");
    formData.append("image_url",selectedAvatar);
    formData.append("content",content);
    formData.append("unique_id","3");
    console.log(formData)
    axios.post(backendURL+"/create-video",formData)
      .then((res)=>{
        // to be verified once
        console.log(res.data.data,res.data);
        setVideosrc(res.data.data);
        handleStepChange();
      }
      ).catch((err)=>{
        console.log(err);
      });
  }

  const handleStepChange = () => {
    setStep(()=>step+1);
  }

  const preview_img = () => {
    const reader = new FileReader();
    reader.addEventListener("load",()=>{
      document.querySelector("#new-avt").src = reader.result;
    });

    reader.readAsDataURL(file.file);
    return (
      <img src='' id='new-avt'></img>
    );
  }

  
  switch (step) {
    case 1:
      return (
        <div className='ehub'>
          <div className="hdg-txt">Module Creation </div>
          <div className="hr-50"></div>
          <br />
          <div className="hdg2-txt">Step 1: Pointers </div>
          <div className="hdg2-txt">Step 2: Content Generation </div>
          <div className="hdg2-txt">Step 3: Avatar Selection </div>
          <div className="hdg2-txt">Step 4: Video Generation </div>
            <textarea 
              name="" 
              id="" 
              cols="30" 
              rows="2"
              className='topic-input'
              onChange={handleTopicChange}
              value={topic}
              placeholder='Enter Topic here....'
            ></textarea>
            <textarea
              name=""
              id=""
              cols="30" 
              rows="10"
              className='pointer-input' 
              onChange={handlePointersChange}
              value={pointers}
              placeholder='Enter your pointers here....'
            ></textarea>
          <button className='pointer-submit-button' onClick={getContentFromPointers}>Next</button>
        </div>
      );
    case 2:
      return (
        <div className='ehub'>
          <div className="hdg-txt">Module Creation </div>
          <div className="hr-50"></div>
          <br />
          <div className="hdg2-txt">Step 1: Pointers </div>
          <div className="hdg2-txt">Step 2: Content Generation </div>
          <div className="hdg2-txt">Step 3: Avatar Selection </div>
          <div className="hdg2-txt">Step 4: Video Generation </div>
          <textarea 
            name=""
            id=""
            cols="30"
            rows="16"
            className='content-input'
            onChange={handleContentChange}
            value={content}
            placeholder='Content from your pointers comes here and can be edited....'
          >
          </textarea>
          <button className='back-button' onClick={reverseStep}>Prev</button>
          <button className='content-submit-button' onClick={handlesubmitContent}>Next</button>
        </div>
      );
    case 3:
      return (
        <div className='ehub'>
          <div className="hdg-txt">Module Creation </div>
          <div className="hr-50"></div>
          <br />
          <div className="hdg2-txt">Step 1: Pointers </div>
          <div className="hdg2-txt">Step 2: Content Generation </div>
          <div className="hdg2-txt">Step 3: Avatar Selection </div>
          <div className="hdg2-txt">Step 4: Video Generation </div>

          <div className="avatars-container">
            <div className="avatar-cards">
              <label htmlFor="avt-upload" className='create-avt-btn'>+</label>
              <input type='file' onChange={handleFileChange} id='avt-upload' hidden />
              {avatar_links.map((element,index) => {
                return (
                  <button key={index} onClick={()=>{handleAvatarSelect(index)}}>
                    {element==selectedAvatar ? <img src={backendURL+element} alt="" key={index} style={{border: "5px solid red"}}/>:
                    <img src={backendURL+element} alt="" key={index}/>}
                  </button>
                )
              })}
              {
                file.file?
                <div className="uploaded-avt-img">
                  {preview_img()}
                  <button onClick={()=>{setFile({file:null})}}>Cancel</button>
                  <button onClick={createAvatar}>Create Avatar</button>
                </div>
                :
                <></>
              }
            </div>
          </div>
          <button className='back-button' onClick={reverseStep}>Prev</button>
          <button className='content-submit-button' onClick={getVideo}>Next</button>
        </div>
      );
    default:
      return(
        <div className='ehub'>
          <div className="hdg-txt">Module Creation </div>
          <div className="hr-50"></div>
          <br />
          <div className="hdg2-txt">Step 1: Pointers </div>
          <div className="hdg2-txt">Step 2: Content Generation </div>
          <div className="hdg2-txt">Step 3: Avatar Selection </div>
          <div className="hdg2-txt">Step 4: Video Generation </div>

          <div className="vid-container">
            <video src={backendURL+videosrc} autoPlay="true" controls="true" className='avatar-vid'></video>
            Content:
            <div className='vid-content'>
              {content}
            </div>
            <button>Publish</button>
          </div>
        </div>
      );
  }
}