from django.shortcuts import render
from .models import Player
from .scrapy import Players
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import PlayerSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from urllib import parse


def store(request):
    url = 'https://www.nba.com/teams'
    try:
        players = Players(url)
        players.store(Player)
        return JsonResponse({'message': 'Storing data successfully.'})
    except:
        return JsonResponse({'message': 'Failure to store data, try again.'})


class MyPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 10


class playerList(APIView):

    def get(self, request, format=None, *args, **kwargs):
        players = Player.objects.order_by('name')
        pagination = MyPagination()
        pageList = pagination.paginate_queryset(players, self.request, self)
        serializer = PlayerSerializer(instance=pageList, many=True)
        return pagination.get_paginated_response(serializer.data)


class playerDetail(APIView):

    def get(self, request, id, format=None, *args, **kwargs):
        player = Player.objects.get(id=id)
        serializer = PlayerSerializer(instance=player)
        return Response(serializer.data)


class AgeList(APIView):

    def get(self, request, age, format=None, *args, **kwargs):
        players = Player.objects.filter(age=age).order_by('name')
        pagination = MyPagination()
        pageList = pagination.paginate_queryset(players, self.request, self)
        serializer = PlayerSerializer(instance=pageList, many=True)
        return pagination.get_paginated_response(serializer.data)


class YearsList(APIView):

    def get(self, request, years, format=None, *args, **kwargs):
        players = Player.objects.filter(years_in_nba=years).order_by('name')
        pagination = MyPagination()
        pageList = pagination.paginate_queryset(players, self.request, self)
        serializer = PlayerSerializer(instance=pageList, many=True)
        return pagination.get_paginated_response(serializer.data)


class PosList(APIView):

    def get(self, request, position, format=None, *args, **kwargs):
        players = Player.objects.filter(position=position).order_by('name')
        pagination = MyPagination()
        pageList = pagination.paginate_queryset(players, self.request, self)
        serializer = PlayerSerializer(instance=pageList, many=True)
        return pagination.get_paginated_response(serializer.data)


class NumList(APIView):

    def get(self, request, number, format=None, *args, **kwargs):
        players = Player.objects.filter(number=number).order_by('name')
        pagination = MyPagination()
        pageList = pagination.paginate_queryset(players, self.request, self)
        serializer = PlayerSerializer(instance=pageList, many=True)
        return pagination.get_paginated_response(serializer.data)


class TeamList(APIView):

    def get(self, request, team, format=None, *args, **kwargs):
        team = parse.unquote(team)
        players = Player.objects.filter(team=team).order_by('name')
        pagination = MyPagination()
        pageList = pagination.paginate_queryset(players, self.request, self)
        serializer = PlayerSerializer(instance=pageList, many=True)
        return pagination.get_paginated_response(serializer.data)


