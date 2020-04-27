from django.test import TestCase

from users.models import User
from users.roles import Roles


REGISTRATION_PATH = "/api/v1/registration"
DEFAULT_USERNAME = "default_user"
DEFAULT_PASSWORD = "default_password"
DEFAULT_EMAIL = "default_email@email.com"


class RegistrationTestCase(TestCase):
    def setUp(self) -> None:
        self.default_user_data = {
            "username": DEFAULT_USERNAME,
            "password": DEFAULT_PASSWORD,
            "email": DEFAULT_EMAIL,
        }
        User.objects.create_user(**self.default_user_data)

    def test_registration_success(self):
        data = {
            "username": "test",
            "password": "password",
            "password_2": "password",
            "email": "test@email.com",
        }

        response = self.client.post(REGISTRATION_PATH, data=data)
        self.assertEqual(response.status_code, 201)

    def test_registration_response_correct(self):
        """Test checks that success registration response
        don't return password."""
        data = {
            "username": "test",
            "password": "password",
            "password_2": "password",
            "email": "test@email.com",
        }

        response = self.client.post(REGISTRATION_PATH, data=data)
        password_in_response = ("password" in response.json()) or (
            "password_2" in response
        )
        self.assertEqual(password_in_response, False)

    def test_registration_email_error(self):
        invalid_email_message = "Enter a valid email address."
        data = {
            "username": "test",
            "password": "password",
            "password_2": "password",
            "email": "test.com",
        }

        response = self.client.post(REGISTRATION_PATH, data=data)
        self.assertEqual(response.status_code, 400)

        response_data = response.json()
        self.assertEqual(response_data["email"][0], invalid_email_message)

    def test_registration_username_is_exist(self):
        error_message = "Username already exist"
        data = {
            "username": DEFAULT_USERNAME,
            "password": "password",
            "password_2": "password",
            "email": "test@email.com",
        }

        response = self.client.post(REGISTRATION_PATH, data=data)
        self.assertEqual(response.status_code, 400)

        response_data = response.json()
        self.assertEqual(response_data["username"][0], error_message)

    def test_registration_email_is_exist(self):
        error_message = "Email already exist"
        data = {
            "username": "test",
            "password": "password",
            "password_2": "password",
            "email": DEFAULT_EMAIL,
        }

        response = self.client.post(REGISTRATION_PATH, data=data)
        self.assertEqual(response.status_code, 400)

        response_data = response.json()
        self.assertEqual(response_data["email"][0], error_message)

    def test_correct_role_after_registration(self):
        """Test checks after registration we set 'author' role to new user."""
        username = "test"
        data = {
            "username": username,
            "password": "password",
            "password_2": "password",
            "email": "test@email.com",
        }

        response = self.client.post(REGISTRATION_PATH, data=data)
        self.assertEqual(response.status_code, 201)

        user = User.objects.get(username=username)
        self.assertEqual(user.role, Roles.AUTHOR.name)
