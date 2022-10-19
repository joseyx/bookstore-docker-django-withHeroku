"""books urls"""
from django.urls import path

# pylint: disable=no-name-in-module
from .views import BookListView, BookDetailView

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
]
