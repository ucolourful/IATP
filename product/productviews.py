from django.shortcuts import render


def product_manage(request):
    return render(request, "product_manage.html")
