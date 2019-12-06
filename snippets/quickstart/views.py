from django.shortcuts import render
from .serializers import UserSerializer, GroupSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User, Group

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer