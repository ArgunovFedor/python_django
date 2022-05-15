from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, db_index=True)
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE
                               ,related_name='advertisements')
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE
                               ,related_name='advertisements')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements'
        ordering = ['title']


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100)