from django.http import HttpResponse


def sayhi(request, name):
    return HttpResponse('Say hi from view function! ' + name)
