"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
import xadmin
# 以下是测试用的
from goods.views_base import GoodsListView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'admin', xadmin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),  # 图片路径
#     商品列表页
#     path('goods/',include('goods.urls')),
    path('goods/',GoodsListView.as_view(),name='goods_list'),

]
