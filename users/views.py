# -*- coding: utf-8 -*-
# python
import requests
# rest_framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
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


# users/resetpassword
# 注册
@authentication_classes((TokenAuthentication,SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class Reset(APIView):

    def post(self, request, format=None):
        user = self.request.user
        try:
            oldPassword = request.POST['oldPassword']
            newPassword = request.POST['newPassword']
        except:
            return HttpResponse(status=400)
        # 判断旧密码是否正确
        exact = authenticate(username=user.username, password=oldPassword)
        if exact is not None:
            myuser = User.objects.get(id=user.id)
            myuser.set_password(newPassword)
            myuser.save()
            # 每重置密码一次，都要更新token
            oldtoken = Token.objects.get(user_id=myuser.id)
            oldtoken.delete()
            token = Token.objects.create(user=myuser)
            results = {'expire':3600,'token':token.key,'username':myuser.username,'id':myuser.id}
            return Response(results)
        else:
            return HttpResponse(status=404)
