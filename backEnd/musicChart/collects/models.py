# -*- coding: utf-8
# python
import json
# django
from django.db import models


class Collect(models.Model):
    user_id = models.IntegerField(default=0)
    music_id = models.IntegerField(default=0)
    status = models.IntegerField(default=1)
