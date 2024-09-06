from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)  #员工账号
    password = models.CharField(max_length=20)  #密码

    def toDict(self):
        return {'username':self.username,'password':self.password,}

    class Meta:
        db_table = 'myusers'
