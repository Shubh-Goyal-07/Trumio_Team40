from rest_framework import generics
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProjectSession, ChatSession
from .serializers import ProjectSessionSerializer, ChatSessionSerializer
from .bot_embedder import parser, split_doc_to_chunk, get_embedding_model, make_vecdb, make_vecdb_for_project
from .bot import bot_loader, get_response
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import AllowAny


projectidToLink={}

    
class InitiateSession(APIView):
    queryset = ProjectSession.objects.all()
    serializer_class = ProjectSessionSerializer
    def post(self, request):
        project_id = request.data.get('project_id')
        project_link = request.data.get('project_link')
        user_id = request.data.get('user_id')
        session_id = project_id+"|"+user_id
            
        if(project_id not in projectidToLink or (project_id in projectidToLink and projectidToLink[project_id] != project_link)):
            vec_db = make_vecdb_for_project(project_id,project_link)
            if(vec_db is None): return Response(status=400,data="Error loading PDF")
            projectidToLink[project_id] = project_link
        res = bot_loader(session_id, project_id)
        return Response(res)


class Chat(APIView):
    permission_classes = [AllowAny]
    queryset = ChatSession.objects.all()
    serializer_class = ChatSessionSerializer
    def post(self, request):
        session_id = request.data.get('project_id')+"|"+request.data.get('user_id')
        question = request.data.get('question')
        print("session_id: ", session_id)
        print("question: ", question)
        
        res = get_response(session_id, question)
        return Response(res)






