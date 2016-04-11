# -*- coding: utf-8
# django
from django.db import models
from musics.models import Music



class Setlist(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=250, default="")
    # collects = models.IntegerField(default=0)
    # comments = models.IntegerField(default=0)
    time = models.DateTimeField(default=0)
    photoUrl = models.ImageField(upload_to='photos/%Y/%m/%d')
    # 歌单类型0，为普通歌单，1为专辑
    list_type = models.IntegerField(default=0)
    # 专辑歌手，list_type为1是才有效
    singer = models.CharField(max_length=100, default="", blank=True)
    musics = models.ManyToManyField(Music, through='SetlistMusic', through_fields=('setlist','music'))

    def __unicode__(self):
        return self.name


class SetlistMusic(models.Model):
    setlist = models.ForeignKey(Setlist)
    music = models.ForeignKey(Music)
