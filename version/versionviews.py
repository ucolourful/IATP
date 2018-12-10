import json

from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render

from version.models import Version


def get_versions(request):
    # 未登录用户
    if "user" not in request.session:
        return HttpResponse(json.dumps({"status": 1, "msg": "login first"}), content_type="application/json")

    # product_id为必须
    if "product_id" not in request.POST:
        return HttpResponse(json.dumps({"status": 1, "msg": "product_id is required"}), content_type="application/json")

    # 获取该product_id下的版本
    versions = []
    for version in Version.objects.filter(Product=request.POST["product_id"]):
        versions.append(model_to_dict(version))

    return HttpResponse(json.dumps({"status": 0, "msg": versions}), content_type="application/json")


def version_manage(request):
    return render(request, "version_manage.html")
