# psots/urls.py
from django.urls import path

from posts.views import HomePageView

app_name = "posts"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
