from django.urls import re_path, path
from . import views


urlpatterns = [
    re_path(r'^store/$', views.store, name='store'),
    re_path(r'^$', views.countryList.as_view(), name='list'),
    re_path(r'^(?P<id>\d+)/$', views.countryDetail.as_view(), name='detail'),
    re_path(r'^name/(?P<name>.*?)/$', views.countryNameDetail.as_view(), name='name'),
    re_path(r'^capital/(?P<capital>.*?)/$', views.countryCapitalDetail.as_view(), name='capital'),
    re_path(r'^currency/(?P<currency>\w+)/$', views.countryCurrencyList.as_view(), name='currency'),
    re_path(r'^continent/(?P<continent>\w+)/$', views.countryContinentList.as_view(), name='continent'),
]