from django.urls import path
from myweb.views import index

urlpatterns = [

    path('', index.index, name='index'),  # 调用网站首页
    path('myblog',index.myblog_index,name='myblog_index'),  # 调用博客首页

    #  执行博客登录，退出
    path('login', index.login, name='myweb_login'),
    path('dologin',index.dologin,name='myweb_dologin'),
    path('loginout',index.loginout,name='myweb_loginout'),

]
