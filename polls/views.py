from django.http import HttpResponse


def index(request):
    return HttpResponse("按照官方文档走一遍")