# yourapp/serializers.py

from rest_framework import serializers
from .models import UploadedFile, ProjectSession, ChatSession

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'folder_name', 'file']


class ProjectSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSession
        fields = ['id', 'project_id', 'session_id']

class ChatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSession
        fields = ['id', 'session_id', 'question']
