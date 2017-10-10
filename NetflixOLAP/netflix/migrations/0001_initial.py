# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AverageHoursPerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=225)),
                ('content_id', models.IntegerField()),
                ('stream_length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ContentRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=225)),
                ('genre_desc', models.CharField(max_length=225)),
                ('genre_count', models.IntegerField()),
                ('cast_name', models.CharField(max_length=225)),
                ('cast_count', models.IntegerField()),
                ('director_name', models.CharField(max_length=225)),
                ('director_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PopularActor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cast_name', models.CharField(max_length=225)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PopularDirector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=225)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PopularGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_desc', models.CharField(max_length=225)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PopularShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDemographics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=225)),
                ('state', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='UserSatisfaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=225)),
                ('state', models.CharField(max_length=225)),
                ('user_country', models.CharField(max_length=225)),
                ('video_quality', models.IntegerField(max_length=10)),
                ('audio_quality', models.IntegerField()),
                ('subtitle_quality', models.IntegerField(max_length=10)),
                ('content_id', models.IntegerField()),
            ],
        ),
    ]
