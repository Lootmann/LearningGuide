# snippets/admin.py
from django.contrib import admin

from snippets.models import SnippetModel


@admin.register(SnippetModel)
class SnippetModelAdmin(admin.ModelAdmin):
    list_display = ["title", "code_heading"]
