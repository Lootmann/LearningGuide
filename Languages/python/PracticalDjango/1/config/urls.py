# config/urls.py
from django.contrib import admin
from django.urls import path, include

from snippets.views import top

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", top, name="top"),
    path("snippets/", include("snippets.urls")),
]
