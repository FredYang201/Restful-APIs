from django.db import models

# Create your models here.

class UserInfo(models.Model):
	USER_TYPE = (
		(1, 'Normal'),
		(2, 'VIP'),
		(3, 'SVIP'),
	)
	userType = models.IntegerField(choices=USER_TYPE)
	userName = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=20)

	class Meta:
		db_table = 'userinfo'


class UserToken(models.Model):
	user = models.OneToOneField("UserInfo", on_delete=models.CASCADE)
	token = models.CharField(max_length=50)

	class Meta:
		db_table = 'usertoken'


