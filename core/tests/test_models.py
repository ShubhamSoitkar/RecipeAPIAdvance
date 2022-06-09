"""
Test for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
#get_user_model helper function is provided by Django in order to get the default user  model for the project.


class ModelTests(TestCase):
    """Tests model"""

    def test_create_user_with_email_successful(self):
        """creating a user with email successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
        #The password that's saved with the user is actually a hashed password So we want to test that the password is correct.
        # And in order to do that, we need to use the check password method that is provided by the default model
        # manager that we add to our project.

    def test_new_user_email_normalized(self):
        """Test email is nromalize for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com','test1@example.com'],
            ['Test2@Example.com','Test2@example.com'],
            ['TEST3@EXAMPLE.COM','TEST3@example.com'],
            ['test4@example.COM','test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email,'sample123')

            self.assertEqual(user.email,expected)


    def test_new_user_without_email_raises_error(self):
        '''Test that creating a user without an email raises a value error.'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','test123')


    def test_create_superuser(self):
        '''test creating a superuser.'''
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)