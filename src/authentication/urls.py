from django.urls import path
from .views import UserRegistrationView, UserLoginView, AccountVerificationView

app_name = "authentication"

urlpatterns = [
    path("register", UserRegistrationView.as_view(), name="register"),
    path("login", UserLoginView.as_view(), name="login"),
    path(
        "activate_account/<uidb64>/<token>/",
        AccountVerificationView.as_view(),
        name="activate_account",
    ),
]
