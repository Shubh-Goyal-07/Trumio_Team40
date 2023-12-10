# yourapp/serializers.py

from rest_framework import serializers
from .models import ProjectSession, ChatSession

class ProjectSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSession
        fields = '__all__'

class ChatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSession
        fields = '__all__'