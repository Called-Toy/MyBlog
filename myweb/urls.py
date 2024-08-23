from django.urls import path
from myweb.views import index
urlpatterns = [
    path('', index.index, name='index'),  # 调用商店首页视图函数
]