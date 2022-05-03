from django.urls import path

from pages.views import xss_view

app_name = "pages"

urlpatterns = [
    path("", xss_view, name="index"),
]
