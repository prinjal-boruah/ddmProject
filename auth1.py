from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework import viewsets,generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User

from . models import Users, Page , Role
from . serializers import UsersSerializer,UsersUpdateSerializer, PageSerializer, RoleSerializer,RoleUpdateSerializer,UserSerializer
from rest_framework.status import (
                                    HTTP_400_BAD_REQUEST,
                                    HTTP_404_NOT_FOUND,
                                    HTTP_200_OK
                                    )

#---------------User Login------------------------------------------------------

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, "user_id":user.id},
                    status=HTTP_200_OK)

#--------------User Registration---------------------

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def Register(request):
    username = request.data.get("username")                                     #request.user.username
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)

    user = User()

    user.username = username
    user.set_password(password)
    user.save()
    return Response({'User Created Successfully': True},
                    status=HTTP_200_OK)
