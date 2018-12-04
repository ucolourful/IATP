import json

from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect

from usersetting.models import UserSetting


# 登录页
def login(request):
    # 已登录,进入主页
    if "user" in request.session:
        return redirect('/home/')

    # POST中不存在'username' or 'password',返回login页面
    if ("username" or "password") not in request.POST:
        return render(request, "login.html")

    # POST中同时存在'username' and 'password',验证用户
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        # 用户验证成功 -> 返回Json，登录成功
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            return HttpResponse(json.dumps({"status": 0, "msg": "登录成功，即将跳转到首页..."}),
                                content_type="application/json")

        # 用户验证失败 -> 返回Json，登录失败
        return HttpResponse(json.dumps({"status": 1, "msg": "登录失败，用户名或密码错误"}),
                            content_type="application/json")


# 主页
def home(request):
    # 未登录，重定向到登录页
    if "user" not in request.session:
        return redirect('/login/')

    # 查询用户配置。若查询条目大于1，删除所有条目，新增一条
    username = request.session["user"]
    if len(UserSetting.objects.filter(username=username)) != 1:
        for u in UserSetting.objects.filter(username=username):
            u.delete()
        usersetting = UserSetting(username=username, product_id=0, product_name="请选择", version_id=0, version_name="请选择")
        usersetting.save()

    # 查询用户配置。查询条目只有一条，返回这条数据
    else:
        usersetting = UserSetting.objects.get(username=username)
    return render(request, "home.html", {"usersetting": usersetting})


# 注销
def logout(request):
    auth.logout(request)
    return redirect('/login/')
