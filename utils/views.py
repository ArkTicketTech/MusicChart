# app
from musics.models import Music
from collects.models import Collect
from comments.models import Comment
from setlists.models import Setlist
from users.models import User


def get_music(userId,musicId):
    music = Music.objects.get(id=musicId)
    try:
        isCollected = Collect.objects.get(user_id=userId, music_id=musicId).status
    except:
        isCollected = 0
    try:
        albumSet = Setlist.objects.raw('SELECT sl.id,sl.name FROM setlists_setlist sl \
            inner join setlists_setlist_musics sm \
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


def get_comment(musicId,setlistId,page):
    startpage = page*20
    comments = Comment.objects.filter(music_id=musicId,setlist_id=setlistId).order_by('-time')[startpage:20]
    results = []
    for c in comments:
        try:
            user = User.objects.get(id=c.user_id)
            user_class = {'id':user.id,'username':user.username,'photoUrl':user.photoUrl}
        pass:
            user_class = {'id':0,'username':;,'photoUrl':'heads/default.jpg'}
        r = {'id':c.id, 'musicId':c.music_id, 'setlistId':c.setlist_id, 'user':user_class, 'time':c.time, 'comment':c.comment}
        results.append(r)
    return results


def get_setlist(setlistId):
    setlist = Setlist.objects.get(id=setlistId)
    setlistmusics = Setlist.objects.raw('SELECT * FROM setlists_setlist_musics where setlist_id=%s',[setlistId])
    result_musics = []
    for setlistmusic in setlistmusics:
        result_musics.append(get_music(0,setlistmusic.music_id))
    result = {'id':setlist.id, 'description':setlist.description, 'musics':result_musics,
                'time':setlist.time, 'photoUrl':setlist.photoUrl.url, 'listType':setlist.list_type,
                'singer':setlist.singer, 'name':setlist.name}
    return result
