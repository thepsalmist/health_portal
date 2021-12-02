from django.shortcuts import redirect, render, reverse
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage, send_mail
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from decouple import config


User = get_user_model()


class UserRegistrationView(View):
    """
    View to handle user registration
    """

    def get(self, request):
        return render(request, "authentication/register.html")

    def post(self, request):
        # request data
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        # validation
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if password != password2:
                    messages.add_message(
                        request, messages.ERROR, "Passwords do not match"
                    )
                else:
                    new_user = User.objects.create_user(username=username, email=email)
                    new_user.set_password(password)
                    new_user.is_active = False
                    new_user.save()

                    # send authentication email
                    # encode uid
                    uidb64 = urlsafe_base64_encode(force_bytes(new_user.pk))
                    # get secure token

                    # get domain
                    domain = get_current_site(request).domain
                    # relative url for emai activation
                    link = reverse(
                        "authentication:activate_account",
                        kwargs={
                            "uidb64": uidb64,
                            "token": token_generator.make_token(new_user),
                        },
                    )
                    activate_link = "http://" + domain + link
                    email_subject = "Activate your account"
                    email_body = (
                        "Hi "
                        + new_user.username
                        + " Welcome to HealthPortal. Use the link below to verify your email address \n"
                        + activate_link
                    )
                    sender_email = config("DEFAULT_FROM_EMAIL")
                    messages.add_message(
                        request, messages.SUCCESS, "account created successfuly"
                    )

        return render(request, "authentication/register.html")


class UserLoginView(View):
    """
    View to login user
    """

    def get(self, request):
        return render(request, "authentication/login.html")

    def post(self, request):
        pass


class AccountVerificationView(View):
    """
    Verify user account via email
    """

    pass
