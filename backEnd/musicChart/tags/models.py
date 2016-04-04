# -*- coding: utf-8
# django
from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50, default="", unique=True)

    def __unicode__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=50, default="", unique=True)

    def __unicode__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=50, default="", unique=True)

    def __unicode__(self):
        return self.name
