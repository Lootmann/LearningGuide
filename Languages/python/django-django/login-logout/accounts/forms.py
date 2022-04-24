# accounts/forms.py
# from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

CustomUserModel = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ("username", "email", "password1", "password2")
