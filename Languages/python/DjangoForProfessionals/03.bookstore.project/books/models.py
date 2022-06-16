# books/models.py
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # ImageField can handle to only image/picture files.
    # when you want to handle to regular file, change ImageField to FileField
    cover = models.ImageField(upload_to="covers/", blank=True)

    class Meta:
        permissions = [
            ("special_status", "Can read all books"),
        ]

    def __str__(self) -> str:
        return str(self.title)

    def get_absolute_url(self) -> str:
        return reverse("books:book_detail", args=[str(self.id)])


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review
