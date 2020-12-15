from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successFool"""
        email = 'test@amirhoseyn.com'
        password = 'passvord'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email domain is normalized"""
        email = 'test@AMIRHOSEYN.COM'
        user = User.objects.create_user(email,'tset321')

        self.assertEqual(user.email,email.lower())

    def test_user_invalid_emial(self):
        """Test Creating user with 9 email raises error"""
        with self.assertRaises(ValueError):
            User.objects.create_user(None,'test321')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = User.objects.create_superuser(
            'test@amirhoseyn.com',
            'test321'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)