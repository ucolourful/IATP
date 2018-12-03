from django.shortcuts import render


def apitest_manage(request):
    return render(request, 'apitest_manage.html')


def apistep_manage(request):
    return render(request, 'apistep_manage.html')


def apis_manage(request):
    return render(request, 'apis_manage.html')
