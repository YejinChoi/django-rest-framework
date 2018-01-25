from django.conf.urls import url
from ep03 import views

urlpatterns = [
    url(r'^post/$',views.PostListAPIView.as_view()),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailAPIView.as_view()),
]