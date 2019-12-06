
from django.contrib import admin
from django.urls import path, re_path, include
from .views import AuthView, OrderView, UserInfoView

urlpatterns = [
    re_path(r'v1/auth/$', AuthView.as_view()),
    re_path(r'v1/order/$', OrderView.as_view()),
    re_path(r'v1/userinfo/$', UserInfoView.as_view()),

]
