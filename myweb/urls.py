from django.urls import path
from myweb.views import index

urlpatterns = [

    path('', index.index, name='index'),  # 调用网站首页
    path('myblog',index.myblog_index,name='myblog_index'),  # 调用博客首页

    #  执行博客登录，退出
    path('myblog/login', index.login, name='myweb_login'),
    path('myblog/dologin',index.dologin,name='myweb_dologin'),
    path('myblog/loginout',index.loginout,name='myweb_loginout'),

    #  添加博客
    path('myblog/add',index.myblog_add,name='myblog_add'),
    #  执行添加博客
    path('myblog/insert',index.myblog_insert,name='myblog_insert'),
    #  编辑博客
    path('myblog/edit/<int:id>',index.myblog_edit,name='myblog_edit'),
    #  执行编辑博客
    path('myblog/update/<int:id>',index.myblog_update,name='myblog_update'),
    #  执行删除博客
    path('myblog/del/<int:id>',index.myblog_del,name='myblog_del'),
    # 确认删除博客
    path('myblog/delconfirm/<int:id>',index.myblog_delconfirm,name='myblog_delconfirm'),

]
