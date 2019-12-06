from django.urls import path, re_path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('store/', views.store, name='store'),
    re_path(r'^$', views.movieList.as_view(), name='list'),
    re_path(r'^(?P<rank>\w+)/$', views.rankList.as_view(), name='rank'),
    re_path(r'^detail/(?P<movieid>\d+)/$', views.movieDetail.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)