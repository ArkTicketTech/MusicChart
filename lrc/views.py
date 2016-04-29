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
from lrc.models import Lrc

# /lrc
# 登陆
class LrcUpload(APIView):

    def post(self, request, format=None):
        try:
            lrc = request.POST['lrc']
        except:
            return HttpResponse(status=400)
        Lrc.objects.create(content=lrc)
        return HttpResponse(status=200)
