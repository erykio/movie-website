# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0005_auto_20171212_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popularperson',
            name='persons',
        ),
        migrations.AddField(
            model_name='popular',
            name='persons',
            field=models.ManyToManyField(blank=True, related_name='popular', to='titles.Person'),
        ),
        migrations.DeleteModel(
            name='PopularPerson',
        ),
    ]
