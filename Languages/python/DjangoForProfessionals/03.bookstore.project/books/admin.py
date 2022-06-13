# books/admin.py
from django.contrib import admin

from books.models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ["title", "author", "price"]
