from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls import include, url
from sample.views import post_list, post_detail

#router = DefaultRouter()
#router.register(r'posts',views.PostViewSet)

urlpatterns = [
    url(r'^posts/$', post_list, name='post-list'),
    url(r'^posts/(?P<pk>\d+)/$', post_detail, name='post-detail'),
    #url(r'', include(router.urls))
]