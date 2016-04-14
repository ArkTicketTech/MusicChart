# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musics', '0002_auto_20160410_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=100)),
                ('description', models.CharField(default=b'', max_length=250)),
                ('time', models.DateTimeField(default=0)),
                ('photoUrl', models.ImageField(upload_to=b'photos/%Y/%m/%d')),
                ('list_type', models.IntegerField(default=0)),
                ('singer', models.CharField(default=b'', max_length=100)),
                ('music', models.ManyToManyField(to='musics.Music')),
            ],
        ),
    ]