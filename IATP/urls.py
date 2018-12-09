"""IATP URL Configuration

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
from django.contrib import admin
from django.urls import path

from IATP import views
from apitest import apiviews
from product import productviews
from version import versionviews

urlpatterns = [
    # 默认页、后台页、登陆页、首页、注销登录
    path('', views.login),
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('home/', views.home),
    path('logout/', views.logout),

    # 产品线&版本管理
    path('product_manage/', productviews.product_manage),
    path('version_manage/', versionviews.version_manage),
    path('products/', productviews.get_products),

    # api接口测试用例管理
    path('apitest_manage/', apiviews.apitest_manage),
    path('apistep_manage/', apiviews.apistep_manage),
    path('apis_manage/', apiviews.apis_manage),
]
