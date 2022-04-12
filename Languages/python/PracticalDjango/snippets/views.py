# snippets/views.py
from django.http import HttpResponse, HttpRequest


def top(request: HttpRequest):
    return HttpResponse(b"Hello World")


def snippet_new(request: HttpRequest):
    return HttpResponse("register snippets")


def snippet_edit(request: HttpRequest, snippet_id: int):
    return HttpResponse("edit snippets")


def snippet_detail(request: HttpRequest, snippet_id: int):
    return HttpResponse("show detail of snippets")
