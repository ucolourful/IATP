import json

from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            return HttpResponse(json.dumps({"status": 0, "msg": "登录成功，即将跳转到首页..."}),
                                content_type="application/json")
        else:
            return HttpResponse(json.dumps({"status": 1, "msg": "登录失败，用户名或密码错误"}),
                                content_type="application/json")
    return render(request, "login.html")


def home(request):
    if "user" not in request.session:
        return render(request, "login.html")

    return render(request, "home.html")
