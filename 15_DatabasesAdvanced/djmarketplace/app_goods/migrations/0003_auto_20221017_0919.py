# Generated by Django 3.2.15 on 2022-10-17 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_goods', '0002_auto_20221017_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='items',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_goods.item'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]