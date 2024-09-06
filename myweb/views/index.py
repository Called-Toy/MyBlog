from django.shortcuts import render, redirect
from myweb.models import User
from django.urls import reverse


# Create your views here.

def index(request):
    return render(request, "myweb/index.html")


# 博客首页
def myblog_index(request):
    return render(request, 'myweb/products/index.html')


#  执行登录表单
def login(request):
    return render(request, "myweb/login.html")


#  提交登录表单
def dologin(request):

    try:
        # 获取表单用户数据
        user = User.objects.get(username=request.POST['username'])
        # 判断登录密码是否正确
        if user.password == request.POST['password']:
            print('登录成功')
            request.session['adminuser'] = user.toDict()
            # 重定向到博客首页
            return redirect(reverse('myblog_index'))
        # 如果密码错误，报错
        else:
            context = {'info:''密码错误！'}
            return render(request, 'myweb/dologin.html', context)
    except Exception as err:
        print(err)
        context = {'info:''登录账号不存在！'}
        return render(request, 'myweb/dologin.html', context)


# 执行退出
def loginout(request):
    # 重定向到登录页
    del request.session['adminuser']
    return redirect(reverse('myweb_login'))
