# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-01 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_auto_20160831_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='rate_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
