# -*- coding: utf-8 -*-
# python
import requests
import time
import datetime
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
from musics.models import Music
from setlists.models import Setlist
from utils.views import get_setlist


# GET /setlists/{setlistId}
# 获取某个歌单
@authentication_classes((TokenAuthentication,SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class SetlistOption(APIView):

    def get(self,request,**kwargs):
        try:
            setlistId = int(self.kwargs['setlistId'])
        except:
            return HttpResponse(status=400)
        try:
            Setlist.objects.get(id=setlistId)
        except:
            return HttpResponse(status=404)
        results = get_setlist(setlistId)
        return Response(results)
