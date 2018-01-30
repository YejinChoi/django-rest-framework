from django.db import models
from django.contrib.auth import settings

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    message = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    created_at = models.DateField(auto_now_add=True)
