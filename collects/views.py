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
# app
from collects.models import Collect
from musics.models import Music


# PUT /collects/{musicId}
# 收藏/取消收藏音乐
@authentication_classes((TokenAuthentication,SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class CollectMusic(APIView):

    def put(self,request,**kwargs):
        try:
            musicId = int(self.kwargs['musicId'])
        except:
            return HttpResponse(status=400)
        try:
            Music.objects.get(id=musicId)
        except:
            return HttpResponse(status=404)
        userId = self.request.user.id
        try:
            collect = Collect.objects.get(user_id=userId,music_id=musicId)
            if collect.status == 0:
                collect.status = 1
            else:
                collect.status = 0
            collect.save()
        except:
            Collect.objects.create(user_id=userId,music_id=musicId,status=1)
        return HttpResponse(status=200)
