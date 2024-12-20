from django.shortcuts import render, redirect
from myweb.models import User, Blog
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
import traceback
from django.core.files.storage import FileSystemStorage
import bcrypt
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return render(request, "myweb/index.html")


# 博客首页
def myblog_index(request):
    # 查询所有博客信息
    blogs = Blog.objects.all()
    # 分页
    paginator = Paginator(blogs, 3)
    page_number = paginator.num_pages
    page_range = paginator.page_range
    page = request.GET.get('page', 1)
    blogs = paginator.get_page(page)
    context = {'products': blogs, 'page_number': page_number, 'page_range': page_range,'page':int(page)}
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
        password = request.POST['password']
        # 密码加密
        password = password.encode('utf-8') # 转为字节串
        salt = bcrypt.gensalt() # 生成盐
        hashed_password = bcrypt.hashpw(password,salt) # 加密
        user.password = hashed_password.decode('utf-8') # 转为字符串
        user.save() # 保存用户信息
        # 保存头像到本地
        avatar = request.FILES['avatar']
        if avatar:
            fs = FileSystemStorage()
            fs.save(avatar.name, avatar)
            user.avatar = avatar.name
        user.save()
        context = {'info': '注册成功！'}
        return render(request, 'myweb/register_success.html', context)
    except Exception as err:
        print(err)
        context = {'info': '注册失败！'}
        return render(request, 'myweb/register_fail.html', context)


def myblog_search(request):
    try:
        keyword = request.GET['keyword']
        blogs = Blog.objects.filter(content__icontains=keyword)
        context = {'products': blogs}
        return render(request, 'myweb/products/index.html', context)
    except Exception as err:
        print(err)
        context = {'info': '搜索失败！'}
        return render(request, 'myweb/products/info.html', context)


#  执行登录表单
def login(request):
    return render(request, "myweb/login.html")


#  提交登录表单
def dologin(request):
    try:
        # 获取表单用户数据
        user = User.objects.get(username=request.POST['username'])

        password = request.POST['password']
        password_encode = password.encode('utf-8')
        # 判断登录密码是否正确
        if  bcrypt.checkpw(password_encode, user.password.encode('utf-8')):
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
