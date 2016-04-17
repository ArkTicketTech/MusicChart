# -*- coding: utf-8 -*-
# python
import requests
#django-rest-framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# django
from django.http import HttpResponse, HttpResponse
from django.db.models import Q
# app
from musics.models import Music
from utils.views import get_music

# GET /musics
# 筛选音乐列表
class Musics(APIView):

    def get(self, request, format=None):
        try:
            page = int(self.request.GET['page'])
        except:
            page = 0
        startpage = page*10
        try:
            userId = self.request.user.id
        except:
            userId = 0
        queryObj = Q()
        try:
            language = str(request.GET['language'])
            queryObj = queryObj & Q(language__name=language)
        except:
            pass
        try:
            style = request.GET['style']
            queryObj = queryObj & Q(style__name=style)
        except:
            pass
        try:
            theme = request.GET['theme']
            queryObj = queryObj & Q(theme__name=theme)
        except:
            pass
        try:
            order = request.GET['order']
        except:
            order = 0
        orderItem = ('time' if (order==0) else 'collects')
        musics = Music.objects.filter(queryObj).order_by(orderItem)[startpage:10]
        results = []
        for music in musics:
            result = get_music(userId,music.id)
            results.append(result)
        response = Response(results)
        response["X-Total-Count"] = musics.count()
        response["Access-Control-Expose-Headers"] = "X-Total-Count"
        return response


# # GET /musics
# # 筛选音乐列表
# @authentication_classes((TokenAuthentication,SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
# class Musics(APIView):
#
#     def get(self, request, format=None):
#         try:
#             page = int(self.request.GET['page'])
#         except:
#             page = 0
#         userId = self.request.user.id
#         startpage = page*10
#         queryObj = Q()
#         try:
#             language = str(request.GET['language'])
#         except:
#             language = ''
#         if language != '':
#             try:
#                 languageObj = Language.objects.get(name=language)
#                 queryObj = queryObj & Q(language=languageObj)
#             except:
#                 return HttpResponse(status=404)
#         try:
#             style = request.GET['style']
#         except:
#             style = ''
#         if style != '':
#             try:
#                 styleObj = Style.objects.get(name=style)
#                 queryObj = queryObj & Q(style=styleObj)
#             except:
#                 return HttpResponse(status=404)
#         try:
#             theme = request.GET['theme']
#         except:
#             theme = ''
#         if theme != '':
#             try:
#                 themeObj = Theme.objects.get(name=theme)
#                 queryObj = queryObj & Q(theme=themeObj)
#             except:
#                 return HttpResponse(status=404)
#         try:
#             order = request.GET['order']
#         except:
#             order = 0
#         orderItem = ('time' if (order==0) else 'collects')
#         musics = Music.objects.filter(queryObj).order_by(orderItem)[startpage:10]
#         results = []
#         for music in musics:
#             result = get_music(userId,music.id)
#             results.append(result)
#         response = Response(results)
#         response["X-Total-Count"] = musics.count()
#         response["Access-Control-Expose-Headers"] = "X-Total-Count"
#         return response

# GET musics/{musicId}
class MusicOption(APIView):

    def get(self, request, format=None):
        try:
            musicId = int(self.kwargs['musicId'])
        except:
            return HttpResponse(status=400)
        try:
            Music.objects.get(id=musicId)
        except:
            return HttpResponse(status=404)
        try:
            userId = self.request.user.id
        except:
            userId = 0
        result = get_music(userId,music.id)
        response = Response(result)
        return response
