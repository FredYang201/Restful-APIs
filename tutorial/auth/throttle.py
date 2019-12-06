VISIT_RECORD = {}
import time
from rest_framework.throttling import BaseThrottle, SimpleRateThrottle

''' 自定义
class VISITTHROTTLE(BaseThrottle):

	def __init__(self):
		self.history = []

	def allow_request(self, request, view):
		# 封装在BaseThrottle中的get_ident()方法
		remote_addr = self.get_ident(request)

		ctime = time.time()
		if remote_addr not in VISIT_RECORD:
			VISIT_RECORD[remote_addr] = [ctime,]

		history = VISIT_RECORD.get(remote_addr)

		self.history = history

		# 有访问记录， 并且最远一次的时间大于60秒，就剔除掉
		while history and history[-1] < ctime - 60:
			history.pop()

		# 不能访问时也不用将时间存入
		if len(history) < 3:
			history.insert(0, ctime)
			return True

		return False

	def wait(self):
		ctime = time.time()
		return 60 - (ctime - self.history[-1])
		
'''


class VisitThrottle(SimpleRateThrottle):
	# 设置一个key, 用来当作rates查找，在settings中查找
	scope = 'Luffy'

	def get_cache_key(self, request, view):
		# 匿名用户IP作为识别符号
		return self.get_indent(request)


class UserThrottle(SimpleRateThrottle):

	scope = 'Luffy_User'

	def get_cache_key(self, request, view):
		# 登录用户用用户名限制
		return request.user.user_name








