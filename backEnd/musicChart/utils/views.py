# app
from musics.models import Music
from collects.models import Collect
from comments.models import Comment


def get_music(userId,musicId):
    music = Music.objects.get(id=musicId)
    try:
        isCollected = Collect.objects.get(user_id=userId, music_id=musicId).status
    except:
        isCollected = 0
    result = {'id':music.id, 'name':music.name, 'language':music.language.name,
            'style':music.style.name, 'theme':music.theme.name, 'collects':music.collects,
            'album':music.album, 'singer':music.singer, 'photoUrl':music.photoUrl,
            'mediaUrl':music.mediaUrl, 'comments':music.comments, 'time':music.time,
            'isCollected':isCollected}
    return result


def get_comment(musicId,page):
    startpage = page*20
    comments = Comment.objects.filter(music_id=musicId).order_by('-time')[startpage:20]
    results = []
    for c in comments:
        r = {'id':c.id, 'musicId':c.music_id, 'userId':c.user_id, 'time':c.time, 'comment':c.comment}
        results.append(r)
    return results
