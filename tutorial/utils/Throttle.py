import time
from rest_framework.throttling import BaseThrottle, SimpleRateThrottle


'''
*****************************************************
	The custom version
*****************************************************

# 访问频次限制
VISIT_RECORD = {}  # 保存访问记录
class MyThrottle(object):
	def __init__(self):
		self.history = []
	def allow_request(self, request, view):
		ctime = time.time()
		remote_addr = request._request.META.get('REOMTE_ADDR')
		# remote_addr = self.get_indent(request)
		if not remote_addr in VISIT_RECORD:
			VISIT_RECORD[remote_addr] = [ctime, ]
		history = VISIT_RECORD[remote_addr]

		self.history = history
		while history and ctime - history[-1] > 60:
			history.pop()

		if len(history) <= 3:
			history.insert(0, ctime)
			return True
		else:
			return False

	def wait(self):
		ctime = time.time()
		return 60 - (ctime - self.history[-1])

'''

class VisitThrottle(SimpleRateThrottle):
	scope = 'Fredyang'
	def get_cache_key(self, request, view):
		return self.get_ident(request)


class UserThrottle(SimpleRateThrottle):
	scope = 'FredYang'
	def get_cache_key(self, request, view):
		# print(request.user)
		return request.user.userName




