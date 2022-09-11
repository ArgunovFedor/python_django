import datetime

import django.utils.timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from djtesting import settings


class Blog(models.Model):
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, db_column="user", on_delete=models.DO_NOTHING)

    def get_absolute_url(self):  # Тут мы создали новый метод
        return reverse('blog_detail', args=[str(self.id)])
