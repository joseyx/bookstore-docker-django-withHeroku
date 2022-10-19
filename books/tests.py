"""books tests"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Book, Review  # pylint: disable=no-name-in-module

# Create your tests here.
class BookTests(TestCase):
    """Book tests"""

    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Harry Potter",
            author="J. K. Rowling",
            price="25.00",
        )

        cls.user = get_user_model().objects.create_user(
            username="reviewuser",
            email="reviewuser@example.com",
            password="password",
        )

        cls.review = Review.objects.create(
            book=cls.book,
            author=cls.user,
            review="An excellent review",
        )

    def test_book_listenig(self):
        """test that book_listenig"""
        self.assertEqual(f"{self.book.title}", "Harry Potter")
        self.assertEqual(f"{self.book.author}", "J. K. Rowling")
        self.assertEqual(f"{self.book.price}", "25.00")

    def test_books_list_view(self):
        """Book list view tests"""
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_books_detail_view(self):
        """Book detail view tests"""
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, "An excellent review")
        self.assertTemplateUsed(response, "books/book_detail.html")
