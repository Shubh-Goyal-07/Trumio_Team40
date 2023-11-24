from rest_framework import serializers

from .models import Pointers, AudioURL


class PointersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pointers
        fields = ['id', 'user_id', 'pointer', 'topic']


class AudioURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioURL
        fields = ['user_id', 'audio_url']