from django.contrib import auth
from django.shortcuts import redirect, render, reverse
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage, send_mail
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from decouple import config

from healthportal import settings
from .utils import token_generator

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
                    sender_email = settings.base.DEFAULT_FROM_EMAIL
                    email = EmailMessage(
                        email_subject,
                        email_body,
                        sender_email,
                        [email],
                    )
                    email.send(fail_silently=False)

                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        "account created successfuly, kindly activate your account",
                    )
                    return redirect("authentication:activate_page")

        context = {"dataValues": request.POST}
        return render(request, "authentication/register.html", context)


class UserLoginView(View):
    """
    View to login user
    """

    def get(self, request):
        return render(request, "authentication/login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(
                        request, messages.SUCCESS, "Welcome to Pepea Health"
                    )
                    return redirect("dashboard:home")
                messages.add_message(
                    request,
                    messages.ERROR,
                    "Your account is not active, check your email to verify your account",
                )
                return render(request, "authentication/login.html")

        messages.add_message(
            request, messages.WARNING, "Invalid credentials, please check again"
        )
        return render(request, "authentication/login.html")


class AccountVerificationView(View):
    """
    Verify user account via email
    """

    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            # check if user is already activated
            if not token_generator.check_token(user, token):
                messages.add_message(
                    request,
                    messages.ERROR,
                    "The activation link is invalid",
                )
                return redirect("authentication:login")

            else:
                if user.is_active:
                    return redirect("authentication:login")
                user.is_active = True
                user.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Welcome! your account has been activated, proceed to login",
                )
                return redirect("authentication:login")

        except Exception as e:
            pass

        return redirect("authentication:login")


class ActivatePageView(View):
    def get(self, request):
        return render(request, "authentication/activate_account.html", context={})


class UserLogoutView(View):
    def post(self, request):
        auth.logout(request)
        return render(request, "authentication/logout.html", context={})
