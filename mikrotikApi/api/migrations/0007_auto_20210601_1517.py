# Generated by Django 3.1.1 on 2021-06-01 20:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210601_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mikrotik',
            name='datetime_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 15, 17, 51, 782273)),
        ),
        migrations.AlterField(
            model_name='mikrotik',
            name='datetime_edit',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 15, 17, 51, 782273)),
        ),
        migrations.AlterField(
            model_name='user',
            name='datetime_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 15, 17, 51, 782273)),
        ),
        migrations.AlterField(
            model_name='user',
            name='datetime_edit',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 15, 17, 51, 782273)),
        ),
    ]