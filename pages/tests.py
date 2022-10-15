"""Pages tests"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView  # pylint: disable=no-name-in-module

# Create your tests here.
class HomePageTests(SimpleTestCase):
    """HomePageTests"""

    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_existes_at_correct_location(self):
        """test_url_existes_at_correct_location"""
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        """test_homepage_url_name"""
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        """test_homepage_template"""
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        """test_homepage_contains_correct_html"""
        self.assertContains(self.response, "home page")

    def test_homepage_does_not_contain_incorrect_html(self):
        """test_homepage_does_not_contain_incorrect_html"""
        self.assertNotContains(self.response, "Hi there!")

    def test_homepage_url_resolves_homepageviews(self):
        """test_homepage_url_resolves_homepageviews"""
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):
    """Test about page"""

    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        """test_aboutpage_status_code"""
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        """test_aboutpage_template"""
        self.assertTemplateUsed(self.response, "about.html")

    def test_aboutpage_contains_correct_html(self):
        """test_aboutpage_contains_correct_html"""
        self.assertContains(self.response, "About Page")

    def test_aboutpage_does_not_contain_incorrect_html(self):
        """test_aboutpage_does_not_contain_incorrect_html"""
        self.assertNotContains(self.response, "Hi there!")

    def test_aboutpage_url_resolves_aboutpageviews(self):
        """test_aboutpage_url_resolves_aboutpageviews"""
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
