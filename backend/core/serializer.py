from rest_framework import serializers

from .models import Pointers, AudioURL, ImageURL, CreateVideo, AvatarURL, Timeline, FlashCard


class PointersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pointers
        fields = ['id', 'user_id', 'pointers', 'topic']


class AudioURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioURL
        fields = ['user_id', 'audio_url']
    
class ImageURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageURL
        fields = ['id','user_id', 'image_url']

class AvatarURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvatarURL
        fields = ['id','user_id', 'image_url']

class CreateVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateVideo
        fields = ['id','user_id','image_url', 'content','unique_id']


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = ['id','project_id', 'project_name', 'weeks']


class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ['project_id', 'project_name', 'summary']