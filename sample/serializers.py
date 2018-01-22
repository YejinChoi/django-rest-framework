from rest_framework import serializers
from .models import Post


#Form과 유사
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'