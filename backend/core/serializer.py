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
        extra_kwargs = {'video_url': {'read_only': True}}
        # exclude = ['video_url']


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = '__all__'
        extra_kwargs = {'timeline': {'read_only': True}}
        # exclude = ['timeline']


class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = '__all__'
        extra_kwargs = {'image': {'read_only': True}}
        # exclude = ['image']