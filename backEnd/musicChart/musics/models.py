# -*- coding: utf-8
# python
import json
# django
from django.db import models



class Music(models.Model):
    name = models.CharField(max_length=100, default="")
    language = models.CharField(max_length=100, default="")
    style = models.CharField(max_length=100, default="")
    theme = models.CharField(max_length=100, default="")
    collects = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    time = models.BigIntegerField(default=0)
    album = models.CharField(max_length=100, default="")
    singer = models.CharField(max_length=100, default="")

    class Meta:
        ordering = ('name',)
