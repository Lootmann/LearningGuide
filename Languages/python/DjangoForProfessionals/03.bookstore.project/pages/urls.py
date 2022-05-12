from django.urls import path

from pages.views import PagesIndexView, PagesAboutView

app_name = "pages"

urlpatterns = [
    path("about/", PagesAboutView.as_view(), name="about"),
    path("", PagesIndexView.as_view(), name="index"),
]
