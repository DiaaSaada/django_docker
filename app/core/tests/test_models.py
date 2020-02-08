from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user(self):
        email = "diaa@gmail.com"
        password = "Test"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ TEst   """

        email = 'test1111@GMAIL.COM'

        user = get_user_model().objects.create_user(
            email=email,
            password="1213131313")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with invalid email rsis error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "123")

    def test_create_new_superuser(self):
        """Test creating new super user"""
        user = get_user_model().objects.create_super_user(
            'super@user.com',
            'password123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
