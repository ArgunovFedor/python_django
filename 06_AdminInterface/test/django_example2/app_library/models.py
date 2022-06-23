from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField(default=5)
    summary = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}'


class Waiter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    biography = models.TextField()
    second_name = models.CharField(max_length=40, default='')
    phone = models.CharField(max_length=16, blank=True)
    personal_page = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    university = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    restaurant = models.ManyToManyField(Restaurant,  on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}. {self.first_name} {self.last_name}'

