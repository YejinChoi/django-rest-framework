from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls import include,url

#router = DefaultRouter()
#router.register(r'posts',views.PostViewSet)

urlpatterns = [
    #url(r'',include(router.urls)),
    url(r'^post/$', views.PostListAPIView.as_view()),
]