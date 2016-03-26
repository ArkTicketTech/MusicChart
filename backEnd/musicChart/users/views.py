# -*- coding: utf-8 -*-
# python
import requests
# rest_framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.authtoken.models import Token
# django
from django.http import HttpResponse
from django.contrib.auth import authenticate
# app
from users.models import User

# users/signin
# 登陆
class Signin(APIView):

    def post(self, request, format=None):
        try:
            username = request.POST['username']
            password = request.POST['password']
        except:
            return HttpResponse(status=400)
        # 判断是否有这个用户名
        try:
            userId = User.objects.get(username=username).id
        except:
            return HttpResponse(status=404)

        user = authenticate(username=username, password=password)
        if user is not None:
            # 每重新登录一次，更新token
            oldtoken = Token.objects.get(user_id=userId)
            oldtoken.delete()
            token = Token.objects.create(user=user)
            results = {'expire':3600,'token':token.key,'username':username,'id':userId}
            return Response(results)
        else:
            return HttpResponse(status=404)


# users/signup
# 注册
class Signup(APIView):

    def post(self, request, format=None):
        try:
            username = request.POST['username']
            password = request.POST['password']
        except:
            return HttpResponse(status=400)
        # 判断是否已存在用户
        try:
            exist = User.objects.get(username=username)
            return HttpResponse(status=409)
        except:
            pass

        user = User.objects.create_user(username=username, password=password)
        userId = user.id
        token = Token.objects.get(user_id=userId)
        results = {'expire':3600,'token':token.key,'username':username,'id':userId}
        return Response(results)
