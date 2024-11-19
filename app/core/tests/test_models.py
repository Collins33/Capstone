"""
Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTestCase(TestCase):
    """Test Models"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.is_freelancer)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_creating_new_user_without_email_raises_error(self):
        """Test that creating a new user without an email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')



    def test_create_superuser(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_super_user(
            email=email,
            password=password,
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_moderator)

    def test_create_superuser(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_super_user(
            email=email,
            password=password,
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_moderator)


    def test_create_employer(self):
        """Test creating an employer is successful."""
        email = 'test_employer@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_employer(
            email=email,
            password=password,
        )

        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_moderator)
        self.assertTrue(user.is_employer)
