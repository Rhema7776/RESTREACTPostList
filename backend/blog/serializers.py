from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    # thumb = serializers.CharField(max_length=200)
