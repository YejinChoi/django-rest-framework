from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from myapp import views

urlpatterns = [
    url('r^view/$',views.myapp_list),
    url('r^(?P<pk>[0-9]+)/$',views.myapp_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)