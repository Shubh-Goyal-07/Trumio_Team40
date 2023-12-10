from django.shortcuts import render
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
import requests
from rest_framework.views import APIView
from .models import Timeline
from .serializer import TimelineSerializer
from .timeline import timeline_generator


class TimelineView(APIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
    @swagger_auto_schema(request_body=TimelineSerializer)
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

        if(len(timeline)==0):
            return Response({"status": "failed","data":"No such project exists"})
        timeline0 = timeline[0]

        splitteddata = timeline0.timeline.split("Week")
        # print(splitteddata)
        weekdata=[]
        for i in splitteddata:
            if(i!=""):
                j=0
                while(j<len(i)):
                    if(i[j]=='T'):
                        break
                    j+=1
                weekdata.append(i[j:])
        
        if(len(weekdata)==int(timeline0.weeks)+1):
            weekdata = weekdata[1:]

        
            
        data = {
            "project_id": timeline0.project_id,
            "project_name": timeline0.project_name,
            "weeks": timeline0.weeks,
            "timeline": weekdata
        }

        return Response({"status": "success","data":data})
    
    