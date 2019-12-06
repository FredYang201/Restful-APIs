from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import UserInfo, UserToken
from django.http import HttpResponse
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import BasePermission
import hashlib
import time


ORDER_DICT = {
	1:{
		'name':'Wife',
		'age': 18,
		'gender': 'male',
		'content': '...'
	},
	2: {
		'name': 'Dog',
		'age': 28,
		'gender': 'male',
		'content': '***'
	},
}


# User authentication
class MyAuthenticate(object):

	def authenticate(self, request, *args, **kwargs):
		token = request._request.GET.get('token')
		obj = UserToken.objects.filter(token=token).first()
		if not obj:
			raise AuthenticationFailed('Failed')
		return (obj.user, obj)

	def authenticate_header(self, request):
		pass


# User permissions
class MyPermission(BasePermission):
	message = 'Please login'
	def has_permission(self, request, *args, **kwargs):
		if request.user.userType != 2:
			return True
		return False


# Encrypted token
def md5(user):
	ctime = str(time.time())
	m = hashlib.md5(bytes(user, encoding='utf-8'))
	m.update(bytes(ctime, encoding='utf-8'))
	return m.hexdigest()


# Login, login success (token return and save to the database)
from .utils.Throttle import VisitThrottle
class AuthView(APIView):
	# The login process does not require permissions or authentication
	permission_classes = []
	authentication_classes = []
	# The login process has a 3/m limits
	throttle_classes = [VisitThrottle, ]

	def post(self, request, *args, **kwargs):
		ret = {'code':1000, 'msg': None}
		try:
			user = request._request.POST.get('userName')
			pwd = request._request.POST.get('password')
			obj = UserInfo.objects.filter(userName=user, password=pwd).first()
			if not obj:
				ret['code'] = 1001
				ret['msg'] = 'Wrong username or password'
			token = md5(user)
			UserToken.objects.update_or_create(user=obj, defaults={'token':token})
			ret['token'] = token
		except Exception as e:
			ret['code'] = 1002
			ret['msg'] = 'Request Error'

		return JsonResponse(ret)


# Order inquiry service
class OrderView(APIView):
	# It uses the default authentication method in Settings
	# It uses the default permissions method in Settings
	# It uses the default throttling 10/m in Settings
	def get(self, request, *args, **kwargs):
		ret = {'code':1000, 'msg':None}
		try:
			ret['data'] = ORDER_DICT
		except Exception as e:
			ret['code'] = 1002
			ret['msg'] = 'Error'
		return JsonResponse(ret)


# User information service
class UserInfoView(APIView):
	# It uses the default authentication method in Settings
	permission_classes = [MyPermission, ]
	# 用的是settings中默认的节流 10/m
	def get(self, request, *args, **kwargs):
		# It uses the default throttling 10/m in Settings
		return HttpResponse('Successfully')





