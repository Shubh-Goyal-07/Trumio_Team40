from django.shortcuts import render
# Create your views here.
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pointers, ImageURL, AvatarURL, CreateVideo, FlashCard
from .serializer import PointersSerializer, ImageURLSerializer, AvatarURLSerializer, CreateVideoSerializer, FlashCardSerializer
from .generate_avatar import generate_avatar
from .generate_lecture import generate_lecture
from .dump_video import dump_video
from .unmark import unmark
from .flashcard import flashcard_text_generator
import time
import json
import environ
env = environ.Env()
environ.Env.read_env()




backendurl = "https://avatar.rohitkori.tech"
DID_API_KEY = env('DID_API_KEY')


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
                return Response({"content" : lect_txt, "status" : "success","data" : serializer.data})
            return Response(serializer.errors)
        else:
            return Response({"status": "failed","data":"Something went wrong"})
    




class ImageURlView(APIView):
    queryset = ImageURL.objects.all()
    serializer_class = ImageURLSerializer
    
    def post(self,request):
        serializer = ImageURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            try:
                avatar_json = generate_avatar(backendurl + serializer.data['image_url'])
                return Response({"status": "success","data":serializer.data,"avatar":avatar_json})
            except:
                return Response({"status": "failed","data":"Something went wrong with the API"})
        return Response(serializer.errors)  

class SaveAvatarURLView(APIView):
    queryset = AvatarURL.objects.all()
    serializer_class = AvatarURLSerializer
    def post(self, request):
        serializer = AvatarURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success","data":serializer.data})
        return Response({"status": "failed","data":serializer.errors})
    
    

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
        print(DID_API_KEY)
        avatar_url = request.POST.get('avatar_url')
        content = request.POST.get('content')
        unique_id = request.POST.get('unique_id')
        user_id = request.POST.get('user_id')
        topic = request.POST.get('topic')
        url = 'https://api.d-id.com/talks'

        serializer = CreateVideoSerializer(data=request.data)
        if serializer.is_valid():
            print("yes")
            # serializer.save()
        else:
            return Response({"status": "failed","data":serializer.errors})
        
        x = unmark(content).replace("\\n"," ")
        y = x.replace("*"," ")
        y = y.replace(":"," ")
        y = repr(" ".join(y.split()))
        print(y)
        print(len(y))


        res_from_post = requests.post(url,
                    headers={
                        "Authorization": "Basic "+DID_API_KEY
                    },
                    json={
                        "script":{
                            "type":"text",
                            "input": str(y[:2000])
                        },
                        "source_url": avatar_url,
                        "provider":{
                            "type": "amazon" 
                        },
                        "face":{
                            "size":1024,
                            "top_left":[0,0]
                        }
                    }
                      )
        return Response(res_from_post.json())
    

class SaveVideoView(APIView):
    def post(self,request):
        avatar_url = request.POST.get('avatar_url')
        content = request.POST.get('content')
        unique_id = request.POST.get('unique_id')
        user_id = request.POST.get('user_id')
        topic = request.POST.get('topic')
        video_url = request.POST.get('video_url')

        pointer = Pointers.objects.filter(id=unique_id).first()

        # dump_video(video_url,unique_id)
        # domainvideourl = f"/media/video/{str(unique_id)}.mp4"
        createvideo_instance = CreateVideo(avatar_url=avatar_url,content = content, user_id = user_id, unique_id = pointer, video_url = video_url, topic = topic)
        createvideo_instance.save()

        return Response({"status": "success", "url":video_url})




class FlashCardView(APIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
    def post(self, request):
        project_id = request.POST.get('project_id')
        project_name = request.POST.get('project_name')
        summary = request.POST.get('summary')

        content = flashcard_text_generator(project_name,summary)
        image = "https://app.thenextleg.io/image/acf4e728-4984-4816-b496-42a44aef0a89/0.png"
        serializer = FlashCardSerializer(data=request.data)
        flashcard_instance = FlashCard(project_id=project_id,project_name=project_name,summary=summary,image=image,content=content)
        if serializer.is_valid():
            flashcard_instance.save()
            return Response({"status": "success","data":serializer.data,"image":image})
        return Response({"status": "failed","data":serializer.errors})
    
    def get(self, request):
        id = request.GET.get('project_id')
        flashcard = FlashCard.objects.filter(project_id=id)
        
        if(len(flashcard)==0):
            return Response({"status": "failed","data":"No data found"})
        flashcard_instance = flashcard[0]

        # print(flashcard_instance.id)
        data = {
            "project_id": flashcard_instance.project_id,
            "project_name": flashcard_instance.project_name,
            "summary": flashcard_instance.summary,
            "image": flashcard_instance.image,
            "content": flashcard_instance.content
        }
        return Response({"status": "success","data":data})
    


class GetLearningModuleView(APIView):
    def get(self, request):
        video = CreateVideo.objects.all()
        serializer = CreateVideoSerializer(video, many=True)
        return Response({"status": "success","data":serializer.data})