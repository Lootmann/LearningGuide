# pages/views.py
from django.http import HttpRequest, HttpResponse


def home_page_view(request: HttpRequest):
    return HttpResponse("Hello, World!")
