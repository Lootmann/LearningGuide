# snippets/admin.py
from django.contrib import admin

from snippets.models import SnippetModel


@admin.register(SnippetModel)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ["title", "text"]
