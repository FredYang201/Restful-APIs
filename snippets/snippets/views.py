from django.shortcuts import render
from .serializers import SnippetSerializerModel, SnippetSerializer
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Snippet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination



'''
1.    FBV
a. Normal function


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def snippetList(request):
    # list all of snippets
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(instance=snippets, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def snippetDetail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return JSONResponse(status=404)
        
    if request.method == 'GET':
        serializer = SnippetSerializer(instance=snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return JSONResponse(status=204)
             

b. Encapsulated function

@api_view(['GET', 'POST'])
def snippetList(request, format=None):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippetDetail(request, pk, format=None):
    print(request.method)
    try:
        snippet = Snippet.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(instance=snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''


class MyPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 6


class SnippetList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request, format=None, *args, **kwargs):
        snippets = Snippet.objects.all()
        paginator = MyPagination()
        pageSnip = paginator.paginate_queryset(snippets, self.request, view=self)
        serializer = SnippetSerializer(instance=pageSnip, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None, *args, **kwargs):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class SnippetDetail(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except:
            return Http404

    def get(self, request, pk, format=None, *args, **kwargs):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(instance=snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None, *args, **kwargs):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None, *args, **kwargs):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
























