# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-01 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20171226_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
