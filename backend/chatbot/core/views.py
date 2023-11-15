from rest_framework import generics
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UploadedFile, ProjectSession, ChatSession
from .serializers import UploadedFileSerializer, ProjectSessionSerializer, ChatSessionSerializer
from .bot_embedder import parser, split_doc_to_chunk, get_embedding_model, make_vecdb, make_vecdb_for_project
from .bot import bot_loader, get_response

class FileUploadView(APIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer

    def post(self,request):
        print(request.data.get('folder_name'))
        print(request.data.get('file'))

        folder_name = request.data.get('folder_name')
        file = request.data.get('file')
        uploads = UploadedFile.objects.create(folder_name=folder_name, file=file)
        make_vecdb_for_project(folder_name)
        return Response({'message': 'Hello, world!'})
    # make_vecdb_for_project(projectid, path)




class FileListView(generics.ListAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer

    

class FileDeleteView(generics.DestroyAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer

    # will automatically trigger when delete request is made
    def perform_destroy(self, instance): 
        # Delete the file from the storage
        file_path = instance.file.path
        if os.path.exists(file_path):
            os.remove(file_path)
        # Delete the database entry
        instance.delete()

    
class InitiateSession(APIView):
    queryset = ProjectSession.objects.all()
    serializer_class = ProjectSessionSerializer
    def post(self, request):
        session_id = request.data.get('session_id')
        project_id = request.data.get('project_id')
        print("session_id: ", session_id)
        print("project_id: ", project_id)
        
        res = bot_loader(session_id, project_id)
        return Response(res)

class Chat(APIView):
    queryset = ChatSession.objects.all()
    serializer_class = ChatSessionSerializer

    def post(self, request):
        session_id = request.data.get('session_id')
        question = request.data.get('question')
        print("session_id: ", session_id)
        print("question: ", question)
        
        res = get_response(session_id, question)
        return Response(res)






