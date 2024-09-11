# 判断是否登录中间件
from django.shortcuts import redirect
from django.urls import reverse
import re
from myweb.models import User
class shopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        path = request.path

        # 判断是否以myblog开头并且不在urllist中
        urllist=['/myblog/login','/myblog/dologin','/myblog/loginout']
        if re.match('^/myblog', path) and path not in urllist:
            # 判断request请求是否携带session
            if 'adminuser' not in request.session:
                return redirect(reverse('myweb_login'))
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
