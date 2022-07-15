# quiz/views.py
from django.views import generic

from quiz.models import QuizModel


class QuizIndexView(generic.ListView):
    model = QuizModel
    template_name = "quiz/index.html"
    context_object_name = "quiz"
