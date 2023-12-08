from django.shortcuts import render
# Create your views here.
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pointers, AudioURL, ImageURL, AvatarURL, CreateVideo, Timeline
from .serializer import PointersSerializer, AudioURLSerializer, ImageURLSerializer, AvatarURLSerializer, CreateVideoSerializer, TimelineSerializer
from .generate_avatar import generate_image
from .generator import generate_lecture
from .dump_video import dump_video
from .flashcard import unmark
from .timeline import timeline_generator
import time
import environ
env = environ.Env()
environ.Env.read_env()








# backendurl = "https://avatar.rohitkori.tech"
SECRET_KEY_API = env('SECRET_KEY_API')

backendurl = "https://avatar.rohitkori.tech/"


class PointersView(APIView):
    queryset = Pointers.objects.all()
    serializer_class = PointersSerializer

    def post(self, request):
        topic = request.POST.get('topic')
        pointers = request.POST.get('pointers')
        print(topic,pointers)
        lect_txt = generate_lecture(topic, pointers)
        print(topic,pointers)
        print(lect_txt)
        if(lect_txt):
            serializer = PointersSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"content" : lect_txt})
            
            return Response(serializer.errors)
        else:
            return Response({"status": "failed","data":"Something went wrong"})
    

class VideoURLView(APIView):
    def get(self, request):
        id = request.GET.get('video_id')
        
        return Response({"status": "success","data":'/media/video/'+str(id)+'.mp4'})
    

class AudioURLView(APIView):
    queryset = AudioURL.objects.all()
    serializer_class = AudioURLSerializer
    def post(self,request):
        serializer = AudioURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"status" : "failed","data" : serializer.errors})
    
    def get(self, request):
        id = request.GET.get('user_id')
        audio = AudioURL.objects.filter(user_id=id)
        serializer = AudioURLSerializer(audio, many=True)
        return Response({"status": "success","data":serializer.data})

class ImageURlView(APIView):
    queryset = ImageURL.objects.all()
    serializer_class = ImageURLSerializer
    
    def post(self,request):
        serializer = ImageURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            generate_image(serializer.data['user_id'], backendurl + serializer.data['image_url'])
            return Response(serializer.data)
        return Response(serializer.errors)

class GetAvatarURLView(APIView):
    queryset = AvatarURL.objects.all()
    serializer_class = AvatarURLSerializer
    def get(self, request):
        id = request.GET.get('user_id')
        image = AvatarURL.objects.filter(user_id=id)
        serializer = AvatarURLSerializer(image, many=True)
        return Response({"status": "success","data":serializer.data})
    

class CreateVideoView(APIView):
    queryset = CreateVideo.objects.all()
    serializer_class = CreateVideoSerializer
    def post(self, request):
        imageURL = request.POST.get('image_url')
        content = request.POST.get('content')
        uniqid = request.POST.get('unique_id')
        url = 'https://api.d-id.com/talks'


        x = unmark(content).replace("\\n"," ")
        y = x.replace("*"," ")
        y = y.replace(":"," ")
        y = repr(" ".join(y.split()))
        print(y)
        print(len(y))

        res_from_post = requests.post(url,
                    headers={
                        "Authorization": "Basic "+SECRET_KEY_API
                    },
                    json={
                        "script":{
                            "type":"text",
                            "input": str(y[:2000])
                        },
                        "source_url": backendurl+str(imageURL),
                        "provider":{
                            "type": "amazon" 
                        }
                    },timeout=500
                      )
        
        print(res_from_post,1)
        if(res_from_post.status_code==400):
            return Response({"status": "failed","data":"Something went wrong"})
        res_from_post = res_from_post.json()
        
        print(res_from_post,2)

        getid = res_from_post.get('id')
        if(getid is None): return Response({"status": "failed","data":res_from_post.get('kind')})
        print(getid)
        
        time.sleep(5)
        res = requests.get(url+'/'+getid,
                    headers={
                        "Authorization": "Basic "+SECRET_KEY_API
                    },)

    
        if(res.status_code==400):
            return Response({"status": "failed","data":"Something went wrong"})
        res = res.json()
        print(res,3)
        
        print(res.get("status"))

        while(res.get("status")!="done"):
            time.sleep(5)
            res = requests.get(url+'/'+getid,
                    headers={
                        "Authorization": "Basic "+SECRET_KEY_API
                    },)
            res = res.json()
            print(res)
            print()
            print()
        print(res)
        videourl = res.get("result_url")
        print(videourl,4)
        dump_video(videourl,uniqid)
        return Response({"status": "success","data":'/media/video/'+str(uniqid)+'.mp4'})
    

class TimelineView(APIView):
    queryset = CreateVideo.objects.all()
    serializer_class = TimelineSerializer
    def post(self, request):
        project_id = request.POST.get('project_id')
        project_name = request.POST.get('project_name')
        weeks = request.POST.get('weeks')
        print(request.data)
        serializer = TimelineSerializer(data=request.data)
        # request.data['timeline'] = timeline_generator(project_name,weeks)
        # serializer = TimelineSerializer(data=request.data)
        timeline = timeline_generator(project_name,weeks)
        timeline_instance = Timeline(project_id=project_id,project_name=project_name,weeks=weeks,timeline=timeline)
        if serializer.is_valid():
            timeline_instance.save()
            return Response({"status": "success","data":serializer.data, "timeline":timeline})
        return Response({"status": "failed","data":serializer.errors})
    
    def get(self, request):
        id = request.GET.get('project_id')
        timeline = Timeline.objects.filter(project_id=id)

        timeline0 = timeline[0]

        splitteddata = timeline0.timeline.split("Week")
        print(splitteddata)
        weekdata=[]
        for i in splitteddata:
            if(i!=""):
                weekdata.append("Week"+i)
            
        data = {
            "project_id": timeline0.project_id,
            "project_name": timeline0.project_name,
            "weeks": timeline0.weeks,
            "timeline": weekdata
        }

        return Response({"status": "success","data":data})
    
    