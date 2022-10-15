from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING),
    score = models.IntegerField(default=0, verbose_name='очки'),
    status = models.CharField(default='Новичок', max_length=100, verbose_name='статус')

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'UserProfile'
