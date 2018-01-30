from rest_framework.serializers import ModelSerializer
from .models import Post
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

        def validate_title(self, title):
             if 'django' not in title:
                 raise ValidationError('제목에 장고를 꼭 포함시켜주세요 ')
                 return title


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['pk', 'username','email']