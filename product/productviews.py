import json

from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render

from product.models import Product


def get_products(request):
    products = []
    # 未登录用户
    if "user" not in request.session:
        return HttpResponse(json.dumps({"status": 1, "msg": products}))

    # 已登录
    for product in Product.objects.all():
        products.append(model_to_dict(product))
    return HttpResponse(json.dumps({"status": 0, "msg": products}), content_type="application/json")


def product_manage(request):
    return render(request, "product_manage.html")