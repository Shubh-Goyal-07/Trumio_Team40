from rest_framework import serializers

from .models import Pointers


class PointersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pointers
        fields = ['id', 'user_id', 'pointer', 'topic']
