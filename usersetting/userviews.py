import json

from django.forms import model_to_dict
from django.http import HttpResponse

from usersetting.models import UserSetting


def userset(request):
    # 未登录用户
    if "user" not in request.session:
        return HttpResponse(json.dumps({"status": 1, "msg": "login first"}), content_type="application/json")

    # 查询用户配置。若查询条目大于1，删除所有条目，新增一条
    username = request.session["user"]
    if len(UserSetting.objects.filter(username=username)) != 1:
        for u in UserSetting.objects.filter(username=username):
            u.delete()
        usersetting = UserSetting(username=username)
        usersetting.save()

    # 查询用户配置。查询条目只有一条，返回这条数据
    else:
        usersetting = UserSetting.objects.get(username=username)

    # 若POST中带有数据，则进行保存
    if "product_id" in request.POST:
        usersetting.product_id = request.POST["product_id"]
    elif "version_id" in request.POST:
        usersetting.version_id = request.POST["version_id"]
    usersetting.save()
    return HttpResponse(json.dumps({"status": 0, "msg": model_to_dict(usersetting)}), content_type="application/json")
