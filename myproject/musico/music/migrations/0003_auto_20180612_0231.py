# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-12 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20180611_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='image',
            field=models.FileField(upload_to='pictures/'),
        ),
    ]