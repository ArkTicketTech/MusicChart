from django.contrib import admin
from .models import Setlist

# Register your models here.
class SetlistAdmin(admin.ModelAdmin):
    filter_horizontal = ('musics',)
admin.site.register(Setlist,SetlistAdmin)
