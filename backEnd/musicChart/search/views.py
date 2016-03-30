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

# GET /search
# 搜索音乐
@authentication_classes((TokenAuthentication,SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class Search(APIView):

    def get(self, request, format=None):
        try:
            page = request.GET['page']
            startpage = page*10
        except:
            return HttpResponse(status=400)
        try:
            key = request.GET['key']
        except:
            return HttpResponse(status=400)
        Q1 = Q(name=key)
        Q2 = Q(album=key)
        Q3 = Q(singer=key)
        Q4 = Q(name__icontains=key)
        Q5 = Q(album__icontains=key)
        Q6 = Q(singer__icontains=key)
        musics1 = Music.objects.filter(Q1).order_by('-time')
        musics2 = Music.objects.filter(Q2 | Q3 & (~Q1)).order_by('-time')
        musics3 = Music.objects.filter(Q4 | Q5 | Q6 & ~(Q2 | Q3 & (~Q1))).order_by('-time')
        musics = musics1 | musics2 | musics3
        results = []
        for music in musics:
            result = get_music(music.id)
            results.append(result)
        response = Response(results)
        response["X-Total-Count"] = musics.count()
        response["Access-Control-Expose-Headers"] = "X-Total-Count"
        return response
