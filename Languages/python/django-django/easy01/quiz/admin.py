# quiz/admin.py
from django.contrib import admin

from quiz.models import QuizModel


class QuizModelAdmin(admin.ModelAdmin):
    list_display = ("statement", "answer", "created_at", "updated_at")
    ordering = ("statement",)


admin.site.register(QuizModel, QuizModelAdmin)
