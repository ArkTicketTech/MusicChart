# app
from musics.models import Music
from collects.models import Collect
from comments.models import Comment
from setlists.models import Setlist,SetlistMusic


def get_music(userId,musicId):
    music = Music.objects.get(id=musicId)
    try:
        isCollected = Collect.objects.get(user_id=userId, music_id=musicId).status
    except:
        isCollected = 0
    try:
        albumSet = Setlist.objects.raw('SELECT sl.id,sl.name FROM setlists_setlist sl \
            inner join setlists_setlistmusic sm \
            on sm.setlist_id=sl.id where sl.list_type=1')[0]
        album = albumSet.name
    except:
        album = ''
    result = {'id':music.id, 'name':music.name, 'language':music.language.name,
            'style':music.style.name, 'theme':music.theme.name, 'collects':music.collects,
            'album':album, 'singer':music.singer, 'photoUrl':music.photoUrl.url,
            'mediaUrl':music.mediaUrl.url, 'comments':music.comments, 'time':music.time,
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


def get_setlist(setlistId):
    setlist = Setlist.objects.get(id=setlistId)
    musics = SetlistMusic.objects.filter(setlist=setlist.id)
    result_musics = []
    for music in musics:
        result_musics.append(get_music(0,music.id))
    result = {'id':setlist.id, 'description':setlist.description, 'musics':result_musics,
                'time':setlist.time, 'photoUrl':setlist.photoUrl.url, 'listType':setlist.list_type,
                'singer':setlist.singer}
    return result
