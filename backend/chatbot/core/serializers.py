# yourapp/serializers.py

from rest_framework import serializers
from .models import ProjectSession, ChatSession

class ProjectSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSession
        fields = ['id', 'project_id', 'user_id','project_link']

class ChatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSession
        fields = ['id', 'project_id', 'user_id', 'question']
