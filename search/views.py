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
from setlists.models import Setlist
from utils.views import get_music,get_setlist

# GET /musics/search
# 搜索音乐
class Search(APIView):

    def get(self, request, format=None):
        try:
            page = request.GET['page']
        except:
            page = 0
        startpage = page*9
        try:
            key = request.GET['key']
        except:
            return HttpResponse(status=400)
        try:
            userId = self.request.user.id
        except:
            userId = 0
        try:
            order = request.GET['order']
        except:
            order = 0;
        orderItem = ('-time' if (order==0) else '-collects')
        Q1 = Q(name=key)
        Q2 = Q(singer=key)
        Q3 = Q(name__icontains=key)
        Q4 = Q(singer__icontains=key)
        musics1 = Music.objects.filter(Q1).order_by(orderItem)
        musics2 = Music.objects.filter(Q2 & (~Q1)).order_by(orderItem)
        musics3 = Music.objects.filter(Q3 | Q4 & ~(Q2 & (~Q1))).order_by(orderItem)
        musics = (musics1 | musics2 | musics3)[startpage:9]
        results = []
        for music in musics:
            result = get_music(0,music.id)
            results.append(result)
        response = Response(results)
        response["X-Total-Count"] = musics.count()
        response["Access-Control-Expose-Headers"] = "X-Total-Count"
        return response


# GET /setlists/search
# 搜索音乐
class SearchSetlist(APIView):

    def get(self, request, format=None):
        try:
            page = request.GET['page']
        except:
            page = 0
        startpage = page*10
        try:
            key = request.GET['key']
        except:
            return HttpResponse(status=400)
        try:
            userId = self.request.user.id
        except:
            userId = 0
        try:
            order = request.GET['order']
        except:
            order = 0;
        orderItem = ('-time' if (order==0) else '-collects')
        Q1 = Q(name=key)
        Q2 = Q(name__icontains=key)
        setlists1 = Setlist.objects.filter(Q1).order_by(orderItem)
        setlists2 = Setlist.objects.filter(Q2 & (~Q1)).order_by(orderItem)
        setlists = (setlists1 | setlists2)[startpage:10]
        results = []
        for setlist in setlists:
            result = get_setlist(setlist.id)
            results.append(result)
        response = Response(results)
        response["X-Total-Count"] = musics.count()
        response["Access-Control-Expose-Headers"] = "X-Total-Count"
        return response
