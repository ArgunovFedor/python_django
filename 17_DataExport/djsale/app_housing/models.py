from django.urls import reverse

from django.db import models


class TypeOfHouse(models.Model):
    """
    Тип помещения
    """
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'тип помещения'
        verbose_name_plural = 'типы помещений'

    def __str__(self):
        return self.name


class QuantityOfRooms(models.Model):
    """
    Количество комнат
    """
    name = models.CharField(max_length=32)
    count = models.IntegerField()

    class Meta:
        verbose_name = 'количество комнат'
        verbose_name_plural = 'количество комнат'

    def __str__(self):
        return f'{self.name} - {str(self.count)}'


class Housing(models.Model):
    """
    Жилище
    """
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    type_of_house = models.ForeignKey(TypeOfHouse, on_delete=models.DO_NOTHING)
    quantity_of_rooms = models.ForeignKey(QuantityOfRooms, on_delete=models.DO_NOTHING)
    published_at = models.DateTimeField(verbose_name='дата публикации', null=True)


    def get_absolute_url(self):
        return reverse('housing-item', args=[str(self.id)])

    class Meta:
        verbose_name = 'жилье'
        verbose_name_plural = 'жилище'

    def __str__(self):
        return self.name
