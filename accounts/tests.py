"""django_project"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignUpPageView

# Create your tests here.
class CustomUserTests(TestCase):
    """Custom tests for custom users"""

    def test_create_user(self):
        """Create a new user"""
        User = get_user_model()  # pylint: disable=invalid-name
        user = User.objects.create_user(
            username="will", email="will@example.com", password="testpass123"
        )
        self.assertEqual(user.username, "will")
        self.assertEqual(user.email, "will@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Test creating a superuser."""
        User = get_user_model()  # pylint: disable=invalid-name
        admin_user = User.objects.create_superuser(
            username="superadmin", email="superadmin@example.com", password="password"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpPageTests(TestCase):
    """Tests for the SignUp"""

    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template_(self):
        """Tests for the SignUp template"""
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I shouldn't be here.")

    def test_signup_form(self):
        """Test for the signup form."""
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        """Test for the signup view"""
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignUpPageView.as_view().__name__)
