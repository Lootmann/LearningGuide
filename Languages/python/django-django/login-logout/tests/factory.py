# tests/factory.py
from django.contrib.auth import get_user_model

from books.models import BookModel

CustomUser = get_user_model()


def create_user(username: str, email: str, password: str) -> CustomUser:
    return CustomUser.objects.create(username=username, email=email, password=password)


def create_superuser(username: str, email: str, password: str) -> CustomUser:
    return CustomUser.objects.create_superuser(username=username, email=email, password=password)


def create_book(bookname: str) -> BookModel:
    return BookModel.objects.create(name=bookname)
