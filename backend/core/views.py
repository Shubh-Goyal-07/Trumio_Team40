from django.shortcuts import render
# Create your views here.
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pointers, AudioURL, ImageURL, CreateVideo
from .serializer import PointersSerializer, AudioURLSerializer, ImageURLSerializer, CreateVideoSerializer
from .dump_video import dump_video
import time

import environ
env = environ.Env()
environ.Env.read_env()
SECRET_KEY_API = env('SECRET_KEY_API')

class PointersView(APIView):
    queryset = Pointers.objects.all()
    serializer_class = PointersSerializer

    def post(self, request):
        serializer = PointersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

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
        return Response(serializer.errors)
    
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
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        id = request.GET.get('user_id')
        image = ImageURL.objects.filter(user_id=id)
        serializer = ImageURLSerializer(image, many=True)
        return Response({"status": "success","data":serializer.data})
    

class CreateVideoView(APIView):
    queryset = CreateVideo.objects.all()
    serializer_class = CreateVideoSerializer
    def post(self, request):
        image_id = request.GET.get('image_id')
        image = ImageURL.objects.filter(id=image_id)
        serializer = ImageURLSerializer(image, many=True)
        if(len(serializer.data)==0):
            return Response({"status": "failed","data":"no image found"})
        image_url = serializer.data[0]['image_url']

        pointer_id = request.GET.get('pointer_id')
        pointer = Pointers.objects.filter(id=pointer_id)
        serializer = PointersSerializer(pointer, many=True)
        if(len(serializer.data)==0):
            return Response({"status": "failed","data":"no pointer found"})
        pointer_text = serializer.data[0]['pointer']


        url = 'https://api.d-id.com/talks'

        res_from_post = requests.post(url,
                    headers={
                        "Authorization": "Basic "+SECRET_KEY_API
                    },
                    json={
                        "script":{
                            "type":"text",
                            "input": pointer_text #need to get actual content from llm
                        },
                        "source_url": "backendurl"+str(image_url),
                    }
                      )
        if(res_from_post.status_code=='400'):
            return Response({"status": "failed","data":"Something went wrong"})
        getid = res_from_post['id']

        time.sleep(secs=10)
        res = requests.get(url+'/'+getid,
                    headers={
                        "Authorization": "Basic "+SECRET_KEY_API
                    },)
        if(res.status_code=='400'):
            return Response({"status": "failed","data":"Something went wrong"})
        
        if(res["status"]=="created"):
            videourl = res["result_url"]
            dump_video(videourl,pointer_id)
            return Response({"status": "success","data":'/media/video/'+str(pointer_id)+'.mp4'})
        elif(res["status"]=="started"):
            time.sleep(secs=5)
            res = requests.get(url+'/'+getid,
                    headers={
                        "Authorization": "Basic Z295YWwuMjJAaWl0ai5hYy5pbg:aPBZD7T5PJvo3Wgkepy6E"
                    },)
            if(res["status"]=="created"):
                videourl = res["result_url"]
                dump_video(videourl,pointer_id)
                return Response({"status": "success","data":'/media/video/'+str(pointer_id)+'.mp4'})
            else:
                return Response({"status": "failed","data":"something went wrong"})

        elif(res["status"]=="rejected" or res["status"]=="error"):
            return Response({"status": "failed","data":"rejected"})

        return Response({"status": "success","data":"something went wrong"})