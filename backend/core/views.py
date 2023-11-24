from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pointers, AudioURL, ImageURL    
from .serializer import PointersSerializer, AudioURLSerializer, ImageURLSerializer

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
    

