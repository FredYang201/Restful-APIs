from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .. import models

class Authenticate(BaseAuthentication):

	def authenticate(self, request, *args, **kwargs):
		token = request._request.GET.get('token')
		token_obj = models.UserToken.objects.filter(token=token).first()
		print(token_obj)
		if not token_obj:
			# This error is caught in the function in the view
			raise exceptions.AuthenticationFailed("User authentication failed.")
		# request.user, request.auth 参数
		# 而token_obj.user中的user与否是因为在models中的名字是user

		return (token_obj.user, token_obj.token)