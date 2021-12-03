from django.test import TestCase
from django.urls import reverse

from authentication.views import User


class BaseTest(TestCase):
    def setUp(self) -> None:
        self.register_url = reverse("authentication:register")
        self.login_url = reverse("authentication:login")
        self.user = {
            "username": "testuser",
            "email": "testuser@gmail.com",
            "password": "temppass",
            "password2": "temppass",
        }
        self.user_wrong_pass = {
            "username": "testuser",
            "email": "testuser@gmail.com",
            "password": "temppass",
            "password2": "tempPass0",
        }
        return super().setUp()


class RegisterTest(BaseTest):
    def test_can_view_register_page(self):
        res = self.client.get(self.register_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "authentication/register.html")

    def test_user_can_register(self):
        res = self.client.post(self.register_url, self.user, format="text/html")
        self.assertEqual(res.status_code, 302)

    def test_user_cant_register_wrong_password(self):
        res = self.client.post(
            self.register_url, self.user_wrong_pass, format="text/html"
        )
        self.assertNotEqual(res.status_code, 302)

    def test_user_cant_register_existing_username(self):
        self.client.post(self.register_url, self.user, format="text/html")
        res = self.client.post(self.register_url, self.user, format="text/html")
        self.assertNotEqual(res.status_code, 302)


class LoginTest(BaseTest):
    def test_can_view_login_page(self):
        res = self.client.get(self.login_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "authentication/login.html")

    def test_successful_login(self):
        self.client.post(self.register_url, self.user, format="text/html")
        user = User.objects.filter(email=self.user["email"]).first()
        user.is_active = True
        user.save()
        res = self.client.post(self.login_url, self.user, format="text/html")
        self.assertEqual(res.status_code, 302)
