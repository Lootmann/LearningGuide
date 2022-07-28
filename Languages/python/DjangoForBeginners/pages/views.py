# pages/views.py
from django.http import HttpResponse, HttpRequest


def HomepageView(request: HttpRequest):
    return HttpResponse("Hello World !")
