# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-12 02:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20180612_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 12, 2, 38, 46, 84735, tzinfo=utc)),
        ),
    ]