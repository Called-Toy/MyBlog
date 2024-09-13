from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)  # 员工账号
    password = models.CharField(max_length=255)  # 密码
    avatar = models.TextField(max_length=20)  # 头像

    def toDict(self):
        return {'username':self.username,'password':self.password,'avatar':self.avatar}

    class Meta:
        db_table = 'myusers'


class Blog(models.Model):
    id = models.AutoField(primary_key=True)  #博客编号
    title = models.CharField(max_length=50)  #标题
    content = models.TextField()  #内容
    created_at = models.DateTimeField(auto_now_add=True)  #创建时间

    class Meta:
        db_table = 'myblogs'