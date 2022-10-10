from django.db import models


class Author(models.Model):
    """Модель автора."""
    name = models.CharField(max_length=200, verbose_name='Имя')
    surname = models.CharField(max_length=200, verbose_name='Фамилия')
    year_of_birth = models.IntegerField(verbose_name='Год рождения')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Author'


class Book(models.Model):
    """Модель книги."""
    name = models.CharField(max_length=200, verbose_name='Название')
    isbn = models.CharField(max_length=20, verbose_name='Международный стандартный книжный номер')
    year_of_release = models.IntegerField(verbose_name='Год выпуска')
    number_of_pages = models.IntegerField(verbose_name='Количество страниц')
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
