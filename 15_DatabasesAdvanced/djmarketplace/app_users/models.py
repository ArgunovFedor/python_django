from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=36, blank=True,verbose_name='City')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Date of birth')
    status = models.CharField(max_length=100, default='Новичок', verbose_name='Status')
    balance = models.IntegerField(default=0, verbose_name='Balance')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'UserProfile'
