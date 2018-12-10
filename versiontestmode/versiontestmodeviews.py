import json

from django.forms import model_to_dict
from django.http import HttpResponse

from versiontestmode.models import VersionTestMode


def get_versiontestmodes(request):
    # 未登录用户
    if "user" not in request.session:
        return HttpResponse(json.dumps({"status": 1, "msg": "login first"}), content_type="application/json")

    # version_id为必须
    if "version_id" not in request.POST:
        return HttpResponse(json.dumps({"status": 1, "msg": "version_id is required"}), content_type="application/json")

        # 获取该version_id下的测试模式
    versiontestmodes = []
    for testmode in VersionTestMode.objects.filter(Version=request.POST["version_id"]):
        versiontestmodes.append(model_to_dict(testmode))

    return HttpResponse(json.dumps({"status": 0, "msg": versiontestmodes}), content_type="application/json")
