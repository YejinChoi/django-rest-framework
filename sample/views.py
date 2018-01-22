from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from django.http import HttpResponse, JsonResponse
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt
from sample.forms import PostForm


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
