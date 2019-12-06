from ..models import UserToken
from rest_framework.exceptions import AuthenticationFailed

'''
**********************************************************
	The custom one!
**********************************************************

class MyAuthenticate(object):
	def authenticate(self, request, *args, **kwargs):
		token = request._request.GET.get('token')
		obj = UserToken.objects.filter(token=token).first()
		if not obj:
			raise AuthenticationFailed('Failed')
		return (obj.user, obj)

	def authenticate_header(self, request):
		pass

'''


'''
	Inheritance from BaseAuthentication

'''

from rest_framework.authentication import BaseAuthentication

class MyAuthenticate(BaseAuthentication):
	def authenticate(self, request, *args, **kwargs):
		token = request._request.GET.get('token')
		obj = UserToken.objects.filter(token=token).first()
		if not obj:
			raise AuthenticationFailed('Authentication failed, please login')
		return (obj.user, obj)

