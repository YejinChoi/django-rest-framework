from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    url(r'',include(router.urls)),
]