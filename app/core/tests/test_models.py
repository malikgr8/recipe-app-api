from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        # test creting a new user with an email #
        email = 'test@londonappdev.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # test the email for a new user is normalized
        email = 'test@LONDONAPPDEV.COM'
        user = get_user_model().objects.create_user(email, 'tset123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # Test creating user with no email
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        # Test creating new superuser
        user = get_user_model().objects.create_superuser(
             'test@londonappdev.com',
             'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
