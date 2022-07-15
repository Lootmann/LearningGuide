# quiz/views.py
from django.views import generic

from quiz.forms import QuizCreateForm
from quiz.models import QuizModel


class QuizIndexView(generic.ListView):
    model = QuizModel
    template_name = "quiz/index.html"
    context_object_name = "quizzes"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = QuizCreateForm()
        return context
