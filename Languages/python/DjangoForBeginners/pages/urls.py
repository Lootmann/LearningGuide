# pages/urls.py
from django.urls import path

from pages.views import HomepageView

urlpatterns = [
    path("", HomepageView, name="home"),
]
