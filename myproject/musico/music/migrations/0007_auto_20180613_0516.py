# Generated by Django 2.0.6 on 2018-06-13 05:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20180613_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 5, 16, 17, 229160, tzinfo=utc)),
        ),
    ]
