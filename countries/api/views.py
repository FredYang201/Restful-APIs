from .scrapy import CountryInfo
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .models import Country
from .serializers import CountrySerializer
from urllib.parse import unquote


def store(request):
    url = 'http://example.webscraping.com'
    page = 25
    country = CountryInfo(url, page)
    country.store(Country)
    return JsonResponse({'message': 'Store the countries data successfully.'})


class MyPagination(PageNumberPagination):
    page_size = 15
    page_query_param = 'page'
    page_size_query_param = 'pageSize'
    max_page_size = 15


class countryList(APIView):

    def get(self, request, *args, **kwargs):
        countries = Country.objects.order_by('name')
        myPage =  MyPagination()
        pageList = myPage.paginate_queryset(countries, self.request, self)
        serializer = CountrySerializer(instance=pageList, many=True)
        return myPage.get_paginated_response(serializer.data)


class countryDetail(APIView):

    def get(self, request, id, *args, **kwargs):
        country = Country.objects.get(id=id)
        serializer = CountrySerializer(instance=country)
        return Response(serializer.data)


class countryNameDetail(APIView):

    def get(self, request, name, *args, **kwargs):
        name = unquote(name)
        country = Country.objects.get(name=name)
        serializer = CountrySerializer(instance=country)
        return Response(serializer.data)


class countryCapitalDetail(APIView):

    def get(self, request, capital, *args, **kwargs):
        capital = unquote(capital)
        country = Country.objects.get(capital=capital)
        serializer = CountrySerializer(instance=country)
        return Response(serializer.data)


class countryCurrencyList(APIView):

    def get(self, request, currency, *args, **kwargs):
        currency = unquote(currency)
        countries = Country.objects.filter(currency=currency).order_by('name')
        myPage =  MyPagination()
        pageList = myPage.paginate_queryset(countries, self.request, self)
        serializer = CountrySerializer(instance=pageList, many=True)
        return myPage.get_paginated_response(serializer.data)


class countryContinentList(APIView):

    def get(self, request, continent, *args, **kwargs):
        countries = Country.objects.filter(continent=continent).order_by('name')
        myPage =  MyPagination()
        pageList = myPage.paginate_queryset(countries, self.request, self)
        serializer = CountrySerializer(instance=pageList, many=True)
        return myPage.get_paginated_response(serializer.data)