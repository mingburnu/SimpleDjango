from rest_framework import serializers

from trips.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'photo', 'location', 'created_at')
