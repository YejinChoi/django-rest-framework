from rest_framework.serializers import ModelSerializer,ReadOnlyField
from .models import Post



#fields 를 Post에 대해서만 지정했으므로 아이피확인은 view에서 함
class PostSerializer(ModelSerializer):
    author_username = ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['author_username','message']