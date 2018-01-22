from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from django.http import HttpResponse, JsonResponse
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt
from sample.forms import PostForm



@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        qs = Post.objects.all()
        data = [{'pk' : post.pk, 'message' : post.message } for post in qs] #수동 JSON 직렬화

        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid() :
            post = form.save()
            return HttpResponse(status=201)
        data = form.errors()
        return JsonResponse(data, status=400)


@csrf_exempt #API서버는 별도의 프로그램에서 direct로 POST 요청 보낼 수 있어서 csrf 체크 빼주어야 함
def post_detail(request, pk):
    post = get_object_or_404

    if request.method == 'GET':
        return JsonResponse({'pk' : post.pk , 'message' : post.message })
    elif request.method == 'PUT':
        put = QueryDict(request.body)
        form = PostForm(put, instance=post)

        if form.is_valid():
            post = form.save()
            data = {'pk' : post.pk, 'message' : post.message }
            return JsonResponse(data=data, status=201)
        return JsonResponse(form.errors)
    elif request.method == 'DELETE':
        post.delete()



# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
