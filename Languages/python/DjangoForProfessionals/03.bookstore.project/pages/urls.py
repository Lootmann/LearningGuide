from django.urls import path

from pages.views import PagesIndexView

app_name = "pages"

urlpatterns = [
    path("", PagesIndexView.as_view(), name="index"),
]
