# -*- coding: utf-8
# django
from django.db import models
from tags.models import Language,Style,Theme



class Music(models.Model):
    name = models.CharField(max_length=100, default="")
    language = models.ForeignKey(Language)
    style = models.ForeignKey(Style)
    theme = models.ForeignKey(Theme)
    collects = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    time = models.DateTimeField(default=0)
    album = models.CharField(max_length=100, default="")
    singer = models.CharField(max_length=100, default="")
    photoUrl = models.CharField(max_length=100,blank=True)
    mediaUrl = models.CharField(max_length=100,blank=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name
