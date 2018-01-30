from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    message = models.CharField(max_length=140)
    ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)