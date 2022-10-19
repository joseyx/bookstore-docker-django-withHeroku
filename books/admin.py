"""django register books in admin"""
from django.contrib import admin

from .models import Book, Review  # pylint: disable=no-name-in-module

# Register your models here.


class ReviewInLine(admin.TabularInline):
    """Reviews in admin view config"""

    model = Review


class BookAdmin(admin.ModelAdmin):
    """Books in admin view config"""

    inlines = [
        ReviewInLine,
    ]

    list_display = ("title", "author", "price")


admin.site.register(Book, BookAdmin)
