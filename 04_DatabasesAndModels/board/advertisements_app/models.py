from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, db_index=True, verbose_name='Заголовок')
    price = models.FloatField(verbose_name='цена', default=0)
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements', verbose_name='Статус')
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                             related_name='advertisements', verbose_name='Рубрика')
    author = models.ForeignKey('Author', default=None, null=True, on_delete=models.CASCADE,
                               related_name='author', verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements'
        ordering = ['title']


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'advertisement_status'
        ordering = ['name']


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'advertisement_type'
        ordering = ['name']


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'
        ordering = ['name']
