from rest_framework.routers import DefaultRouter
#from .views import PostViewSet
from django.conf.urls import include, url
from . import views


#router = DefaultRouter()
#router.register(r'posts', PostViewSet)

urlpatterns = [
    #url(r'', include(router.urls)),
    url(r'^posts/$',views.PostListAPIView.as_view()),
]