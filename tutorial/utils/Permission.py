from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
	message = 'No access rights'
	def has_permission(self, request, *args, **kwargs):
		if request.user.userType == 2:
			return True
		return False