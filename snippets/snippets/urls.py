from . import views
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # re_path(r'^$', views.snippetList, name='snippetList'),
    # re_path(r'^(?P<pk>[0-9]+)/$', views.snippetDetail, name='snippetDetail'),
    re_path(r'^$', views.SnippetList.as_view(), name='snippetList'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippetDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)