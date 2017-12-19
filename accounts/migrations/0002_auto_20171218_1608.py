# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='imdb_id',
            field=models.CharField(blank=True, default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='tagline',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
    ]