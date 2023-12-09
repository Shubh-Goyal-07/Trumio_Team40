from rest_framework import serializers

from .models import Pointers, AudioURL, ImageURL, CreateVideo, AvatarURL, Timeline, FlashCard


class PointersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pointers
        fields = '__all__'
        

class AudioURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioURL
        fields = '__all__'
    
class ImageURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageURL
        fields = '__all__'

class AvatarURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvatarURL
        fields = '__all__'

class CreateVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateVideo
        fields = '__all__'
        exclude = ['video_url']


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = '__all__'
        exclude = ['timeline']


class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = '__all__'
        exclude = ['image']