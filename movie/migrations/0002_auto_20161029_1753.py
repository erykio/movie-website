# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-29 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate_date',
            field=models.DateField(),
        ),
    ]