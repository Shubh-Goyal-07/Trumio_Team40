from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pointers
from .serializer import PointersSerializer

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
        
        return Response({"status": "success","data":'/media/'+str(id)+'.mp4'})