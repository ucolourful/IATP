from django.contrib import auth
from django.shortcuts import render, redirect


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
            return redirect('/home/')

        # 用户验证失败 -> 返回Json，登录失败
        return render(request, "login.html", {'error': "用户名或密码错误"})


# 主页
def home(request):
    # 未登录，重定向到登录页
    if "user" not in request.session:
        return redirect('/login/')
    return render(request, "home.html")


# 注销
def logout(request):
    auth.logout(request)
    return redirect('/login/')
