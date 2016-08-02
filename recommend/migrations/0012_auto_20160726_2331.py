# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0011_auto_20160726_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='const',
            field=models.CharField(max_length=50, unique=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='date_insert',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='nick',
            field=models.CharField(max_length=30),
        ),
    ]