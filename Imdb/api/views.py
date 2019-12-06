from django.shortcuts import render
from django.http import JsonResponse
from .scrapy import Scrapy
from .models import Movies
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .serializers import MovieSerializer
from rest_framework.response import Response


def store(request):
    myScrapy = Scrapy('http://www.imdb.com/chart/top')
    myScrapy.store(Movies)
    return JsonResponse({'msg': 'Store movie information successfully.'})


class MyPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 15


class movieList(APIView):
    def get(self, request, format=None, *args, **kwargs):
        movies = Movies.objects.all().order_by('movieId')
        myPage = MyPagination()
        pageList = myPage.paginate_queryset(movies, self.request, view=self)
        serializer = MovieSerializer(instance=pageList, many=True)
        return myPage.get_paginated_response(serializer.data)


class rankList(APIView):

    def get_object(self, rank):
        return Movies.objects.order_by('-' + rank)

    def get(self, request, rank, format=None, *args, **kwargs):
        movies = self.get_object(rank)
        myPage = MyPagination()
        pageList = myPage.paginate_queryset(movies, self.request, view=self)
        serializer = MovieSerializer(instance=pageList, many=True)
        return myPage.get_paginated_response(serializer.data)


class movieDetail(APIView):
    def get(self, request, movieid, format=None, *args, **kwargs):
        try:
            movie = Movies.objects.get(movieId=movieid)
            serializer = MovieSerializer(instance=movie)
            return Response(serializer.data)
        except:
            return Response({"error": "The movie doesn't exist."})
