# accounts/urls.py
from django.urls import path

from accounts.views import CustomLoginView, CustomLogoutView, CustomSignUpView

app_name = "accounts"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("signup/", CustomSignUpView.as_view(), name="signup"),
]
