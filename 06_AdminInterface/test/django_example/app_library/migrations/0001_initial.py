# Generated by Django 2.2 on 2022-06-21 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=50)),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]
