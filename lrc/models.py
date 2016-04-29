from django.db import models
import datetime



class Lrc(models.Model):
    content = models.CharField(max_length=250, default="")
    time = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('time',)

    def __unicode__(self):
        return self.time.strftime("%Y-%m-%d %H:%I:%S")
