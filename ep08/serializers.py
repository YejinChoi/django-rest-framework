from rest_framework.serializers import ModelSerializer
from .models import Post



#fields 를 Post에 대해서만 지정했으므로 아이피확인은 view에서 함
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['message']