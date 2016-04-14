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
    singer = models.CharField(max_length=100, default="", blank=True)
    photoUrl = models.ImageField(upload_to='photos/%Y/%m/%d')
    mediaUrl = models.FileField(upload_to='musics/%Y/%m/%d')

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name
