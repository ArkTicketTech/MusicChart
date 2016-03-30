# app
from musics.models import Music


def get_music(musicId):
    music = Music.objects.get(id=musicId)
    result = {'id':music.id, 'name':music.name, 'language':music.language,
            'style':music.style, 'theme':music.theme, 'collects':music.collects,
            'album':music.album, 'singer':music.singer, 'photoUrl':music.photoUrl,
            'mediaUrl':music.mediaUrl, 'comments':music.comments, 'time':music.time}
    return result
