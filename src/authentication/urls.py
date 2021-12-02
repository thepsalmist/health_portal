from django.urls import path
from .views import UserRegistrationView, UserLoginView

app_name = "authentication"

urlpatterns = [
    path("register", UserRegistrationView.as_view(), name="register"),
    path("register", UserLoginView.as_view(), name="login"),
]
