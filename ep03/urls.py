from django.conf.urls import url,include
from ep03 import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'post', views.PostViewSet)
router.register(r'user', views.UserViewSet)


urlpatterns = [
    #url(r'^post/$',views.PostListAPIView.as_view()),
    #url(r'^post/(?P<pk>\d+)/$', views.PostDetailAPIView.as_view()),
    url(r'',include(router.urls)),
]