import React, { useEffect } from 'react'

export default function Project() {
    var steps = ["Step1","Step2","Step3","Step4","Step5"];
    var step_desc = [
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam ullam expedita nam hic aliquam? Cumque delectus repudiandae qui a praesentium",
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam ullam expedita nam hic aliquam? Cumque delectus repudiandae qui a praesentium Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam ullam expedita nam hic aliquam? Cumque delectus repudiandae qui a praesentium",
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam ullam expedita nam hic aliquam? Cumque delectus repudiandae qui a praesentium",
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam ullam expedita nam hic aliquam? Cumque delectus repudiandae qui a praesentium Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam ullam expedita nam hic aliquam? Cumque delectus repudiandae qui a praesentiumLorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam ullam expedita nam hic aliquam? Cumque delectus repudiandae qui a praesentium",
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam ullam expedita nam hic aliquam? Cumque delectus repudiandae qui a praesentium"
    ]
    
    useEffect(()=>{
        var roadmap = document.getElementsByClassName("roadmap-wrap")[0];
        roadmap.innerHTML = ""
        for(var v=0;v<steps.length;v++){
            var step_case = document.createElement("div");
            var connecter = document.createElement("div");
            var step = document.createElement("div");
            var hdg = document.createElement("div");
            var desc = document.createElement("div");
            
            step_case.classList.add("step-case");
            connecter.classList.add("connector");
            step.classList.add("step");
            hdg.classList.add("hdg");
            desc.classList.add("desc");
            
            hdg.innerHTML = steps[v];
            desc.innerHTML = step_desc[v];

            step.appendChild(hdg);
            step.appendChild(desc);

            step_case.appendChild(connecter);
            step_case.appendChild(step);

            roadmap.appendChild(step_case);
        }
    },[]);

    return (
        <div className='project-tab'>
            <img src="project_about.png" className='proj-about' alt="" />
            <div className="project-tab-right-section">
                <img src="project-subtabs.jpeg" className='project-tab-subtabs' alt="" width="72%"/>
                <div className="roadmap">
                    <div className="section-hdg">Roadmap</div>
                    <div className="roadmap-wrap">

                    </div>
                </div>
            </div>
        </div>
    )
}