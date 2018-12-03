from django.shortcuts import render


def version_manage(request):
    return render(request, "version_manage.html")
