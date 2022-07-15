# quiz/urls.py
from django.urls import path

from quiz.views import QuizIndexView

app_name = "quiz"

urlpatterns = [
    path("", QuizIndexView.as_view(), name="index"),
]
