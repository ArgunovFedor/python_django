# Generated by Django 3.2.15 on 2022-10-06 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('year_of_birth', models.IntegerField(verbose_name='Год рождения')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('isbn', models.CharField(max_length=20, verbose_name='Международный стандартный книжный номер')),
                ('year_of_release', models.IntegerField(verbose_name='Год выпуска')),
                ('number_of_pages', models.IntegerField(verbose_name='Количество страниц')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_electronic_library.author')),
            ],
        ),
    ]
