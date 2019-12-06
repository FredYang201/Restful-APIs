from . import views
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('store/', views.store, name='store'),
    re_path(r'^$', views.playerList.as_view(), name='list'),
    re_path(r'^(?P<id>\d+)/$', views.playerDetail.as_view(), name='detail'),
    re_path(r'^age/(?P<age>\d+)/$', views.AgeList.as_view(), name='age'),
    re_path(r'^year_in_nba/(?P<years>\d+)/$', views.YearsList.as_view(), name='years'),
    re_path(r'^position/(?P<position>\w+)/$', views.PosList.as_view(), name='position'),
    re_path(r'^number/(?P<number>\d+)/$', views.NumList.as_view(), name='number'),
    re_path(r'^team/(?P<team>.*?)/$', views.TeamList.as_view(), name='team'),
]

urlpatterns = format_suffix_patterns(urlpatterns)