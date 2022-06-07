# Generated by Django 2.2 on 2022-06-07 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0013_comments_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='news',
        ),
        migrations.AddField(
            model_name='news',
            name='comments',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='advertisements_app.Comments', verbose_name='Комменты'),
        ),
    ]