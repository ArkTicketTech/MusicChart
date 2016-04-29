"""musicChart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from users.views import Signup,Signin,Reset
from musics.views import Musics,MusicOption
from search.views import Search,SearchSetlist
from comments.views import CommentMusic,CommentSetlist
from collects.views import CollectMusic,CollectSetlist
from setlists.views import SetlistOption,SetlistList,AlbumList
from lrc.views import LrcUpload

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/signup', Signup.as_view()),
    url(r'^users/signin', Signin.as_view()),
    url(r'^users/resetpassword', Reset.as_view()),
    url(r'^musics/(?P<musicId>[0-9]+)$', MusicOption.as_view()),
    url(r'^musics$', Musics.as_view()),
    url(r'^musics/search$', Search.as_view()),
    url(r'^setlists/search$', SearchSetlist.as_view()),
    url(r'^musics/comments/(?P<musicId>[0-9]+)$', CommentMusic.as_view()),
    url(r'^setlists/comments/(?P<setlistId>[0-9]+)$', CommentSetlist.as_view()),
    url(r'^musics/collects/(?P<musicId>[0-9]+)$', CollectMusic.as_view()),
    url(r'^setlists/collects/(?P<musicId>[0-9]+)$', CollectSetlist.as_view()),
    url(r'^setlists$', SetlistList.as_view()),
    url(r'^albums$', AlbumList.as_view()),
    url(r'^setlists/(?P<setlistId>[0-9]+)$', SetlistOption.as_view()),
    url(r'^lrc', LrcUpload.as_view()),
]
