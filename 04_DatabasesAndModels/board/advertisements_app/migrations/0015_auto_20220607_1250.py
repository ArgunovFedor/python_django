# Generated by Django 2.2 on 2022-06-07 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0014_auto_20220607_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='news',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news', to='advertisements_app.News', verbose_name='Новости'),
        ),
    ]
