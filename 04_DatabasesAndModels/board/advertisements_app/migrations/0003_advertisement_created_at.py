# Generated by Django 4.0.4 on 2022-05-14 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0002_advertisement_description_alter_advertisement_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
