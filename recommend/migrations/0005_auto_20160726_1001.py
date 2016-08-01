# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 08:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0004_auto_20160726_0931'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recommendation',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='recommendation',
            name='date_insert',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 26, 8, 1, 5, 811204, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
