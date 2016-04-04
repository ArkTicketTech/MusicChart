# -*- coding: utf-8
# python
import json
# django
from django.db import models


class Comment(models.Model):
    user_id = models.IntegerField(default=0)
    music_id = models.IntegerField(default=0)
    comment = models.CharField(max_length=250, default="")
    time = models.DateTimeField(default=0)
