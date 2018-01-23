from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from django.http import HttpResponse, JsonResponse
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt
from sample.forms import PostForm
from rest_framework import generics


# Create your views here.
#class PostViewSet(viewsets.ModelViewSet):
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
