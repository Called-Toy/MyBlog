from django.shortcuts import render, redirect
from myweb.models import User, Blog
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
import traceback
# Create your views here.

def index(request):
    return render(request, "myweb/index.html")


# 博客首页
def myblog_index(request):
    # 查询所有博客信息
    blogs = Blog.objects.all()
    context = {'products': blogs}
    return render(request, 'myweb/products/index.html', context)


# 添加博客
def myblog_add(request):
    return render(request, 'myweb/products/add.html')


# 执行添加博客
def myblog_insert(request):
    try:
        blog = Blog()
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        context = {'info': '添加成功！'}
    except Exception as err:
        print(err)
        context = {'info': '添加失败！'}
    return render(request, 'myweb/products/info.html', context)


# 编辑博客
def myblog_edit(request,id):
    try:
        blog = Blog.objects.get(id=id)
        context = {'blog': blog}
        return render(request, 'myweb/products/edit.html', context)
    except Exception as err:
        print(err)
        context = {'info': '没有找到要修改的博客！'}
        return render(request, 'myweb/products/info.html', context)
# 执行编辑博客
def myblog_update(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.method == 'POST':
        try:
            blog.title = request.POST.get('title', blog.title)
            blog.content = request.POST.get('content', blog.content)
            blog.save()
            context = {'info': '修改成功！'}
        except Exception as err:
            # 打印详细的堆栈跟踪信息
            print("Error:", err)
            print(traceback.format_exc())
            context = {'info': '修改失败！'}
    else:
        context = {'info': '无效的请求方法'}

    return render(request, 'myweb/products/info.html', context)

# 执行删除博客
def myblog_del(request, id):
    try:
        blog = Blog.objects.get(id=id)
        blog.delete()
        context = {'info': '删除成功！'}
    except Exception as err:
        print(err)
        context = {'info': '删除失败！'}
    return render(request, 'myweb/products/info.html', context)

# 删除确认
def myblog_delconfirm(request, id):
    try:
        blog = Blog.objects.get(id=id)
        context = {'blog': blog}
        return render(request, 'myweb/products/delconfirm.html', context)
    except Exception as err:
        print(err)
        context = {'info': '没有找到要删除的博客！'}
        return render(request, 'myweb/products/info.html', context)



# 注册博客
def register(request):
    return render(request, "myweb/register.html")

# 执行注册
def do_register(request):
    try:
        user = User()
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.avatar = request.POST['avatar']
        user.save()
        # 保存头像到本地
        avatar = request.FILES.get('avatar')
        if avatar:
            with open('/static/myweb/' + user.avatar, 'wb') as f:
                for chunk in avatar.chunks():
                    f.write(chunk)
        context = {'info': '注册成功！'}
        return render(request, 'myweb/register_success.html', context)
    except Exception as err:
        print(err)
        context = {'info': '注册失败！'}
        return render(request, 'myweb/register_fail.html', context)

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
            context = {'info':'密码错误！'}
            return render(request, 'myweb/login_info.html', context)
    except Exception as err:
        print(err)
        context = {'info':'登录账号不存在！'}
        return render(request, 'myweb/login_info.html', context)


# 执行退出
def loginout(request):
    # 重定向到登录页
    del request.session['adminuser']
    return redirect(reverse('myweb_login'))
