# authentication/tests.py

from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

User = get_user_model()

class TestUserModel(APITestCase):
    def test_creates_user(self):
        """
        Test that a regular user is created successfully with valid username, email, and password.
        """
        user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.check_password('testpassword123'))
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.email_verified)

    def test_creates_superuser(self):
        """
        Test that a superuser is created successfully with is_staff and is_superuser set to True.
        """
        superuser = User.objects.create_superuser(
            username='adminuser',
            email='admin@example.com',
            password='adminpassword123'
        )
        self.assertIsInstance(superuser, User)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.check_password('adminpassword123'))
        self.assertEqual(superuser.username, 'adminuser')
        self.assertEqual(superuser.email, 'admin@example.com')
        self.assertTrue(superuser.is_active)
        self.assertFalse(superuser.email_verified)  # Assuming email_verified defaults to False

    def test_if_no_username(self):
        """
        Test that creating a user without a username raises a ValueError.
        """
        with self.assertRaises(ValueError) as context:
            User.objects.create_user(
                username='',
                email='nousername@example.com',
                password='password123'
            )
        self.assertIn("The given username must be set", str(context.exception))

    def test_if_no_email(self):
        """
        Test that creating a user without an email raises a ValueError.
        """
        with self.assertRaises(ValueError) as context:
            User.objects.create_user(
                username='userwithoutemail',
                email='',
                password='password123'
            )
        self.assertIn("The given email must be set", str(context.exception))

    def test_superuser_creation_without_is_staff(self):
        """
        Test that creating a superuser without `is_staff=True` raises a ValueError.
        """
        with self.assertRaises(ValueError) as context:
            User.objects.create_superuser(
                username='adminuser',
                email='admin@example.com',
                password='adminpassword123',
                is_staff=False  # Manually set is_staff to False
            )
        self.assertEqual(str(context.exception), "Superuser must have is_staff=True.")

    def test_superuser_creation_without_is_superuser(self):
        """
        Test that creating a superuser without `is_superuser=True` raises a ValueError.
        """
        with self.assertRaises(ValueError) as context:
            User.objects.create_superuser(
                username='adminuser',
                email='admin@example.com',
                password='adminpassword123',
                is_superuser=False  # Manually set is_superuser to False
            )
        self.assertEqual(str(context.exception), "Superuser must have is_superuser=True.")