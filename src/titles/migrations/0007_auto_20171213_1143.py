# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0006_auto_20171212_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='NowPlaying',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateField(unique=True)),
                ('titles', models.ManyToManyField(blank=True, related_name='nowplaying', to='titles.Title')),
            ],
            options={
                'ordering': ('-titles__release_date',),
            },
        ),
        migrations.AlterField(
            model_name='crewtitle',
            name='job',
            field=models.IntegerField(blank=True, choices=[(0, 'Director'), (1, 'Screenplay'), (2, 'Creator')], null=True),
        ),
    ]
