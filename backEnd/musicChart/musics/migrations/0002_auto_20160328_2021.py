# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-28 12:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={'ordering': ('name',)},
        ),
    ]