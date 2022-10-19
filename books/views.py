"""books views"""
from django.views.generic import ListView, DetailView

# pylint: disable=no-name-in-module
from .models import Book

# Create your views here.
class BookListView(ListView):
    """Book list view"""

    model = Book
    context_object = "book_list"
    template_name = "books/book_list.html"


class BookDetailView(DetailView):
    """Book detail view"""

    model = Book
    context_object = "book"
    templates_name = "books/book_detail.html"
