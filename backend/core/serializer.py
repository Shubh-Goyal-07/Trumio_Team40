from rest_framework import serializers

from .models import Pointers, AudioURL, ImageURL


class PointersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pointers
        fields = ['id', 'user_id', 'pointer', 'topic']


class AudioURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioURL
        fields = ['user_id', 'audio_url']
    
class ImageURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageURL
        fields = ['id','user_id', 'image_url']