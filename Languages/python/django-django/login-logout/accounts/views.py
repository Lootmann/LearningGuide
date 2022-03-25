# accounts/views.py
from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"


class CustomLogoutView(LogoutView):
    template_name = "accounts/logout.html"
