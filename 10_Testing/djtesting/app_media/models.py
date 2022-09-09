from django.db import models

# Create your models here.
from app_blog.models import Blog


class File(models.Model):
    file = models.FileField(upload_to='files/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

