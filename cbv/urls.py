from django.conf.urls import url
#from .views import GreetingView, MorningGreetingView
from . import views

urlpatterns = [
    #url(r'^$', GreetingView.as_view()),
    #url(r'^morning/$', MorningGreetingView.as_view()),
    #url(r'^evening/$', views.evening_greeting),
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit),
]