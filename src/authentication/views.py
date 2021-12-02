from django.shortcuts import render
from django.views.generic import View


class RegistrationView(View):
    """
    View to handle user registration
    """

    def get(self, request):
        return render(request, "authentication/register.html")

    def post(self, request):
        return render(request, "authentication/register.html")
