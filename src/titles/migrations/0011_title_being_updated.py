# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0010_auto_20171216_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='being_updated',
            field=models.BooleanField(default=False),
        ),
    ]
