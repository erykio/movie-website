# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-12 17:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(blank=True, max_length=15, null=True)),
                ('imdb_ratings', models.FileField(blank=True, null=True, upload_to='user_imdb_ratings')),
                ('imdb_ratings_used', models.DateTimeField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='user_avatars')),
                ('ratings_last_updated', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
