# Generated by Django 2.2.5 on 2019-10-19 12:26

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0009_image_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.AlterField(
            model_name='image',
            name='like_count',
            field=models.IntegerField(blank=True, default=0, verbose_name=django.contrib.auth.models.User),
        ),
    ]