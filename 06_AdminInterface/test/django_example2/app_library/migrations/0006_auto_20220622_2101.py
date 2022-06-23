# Generated by Django 2.2 on 2022-06-22 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_library', '0005_remove_test_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='name',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='rating',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='test',
            name='summary',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='test',
            field=models.CharField(default=21, max_length=100),
            preserve_default=False,
        ),
    ]
