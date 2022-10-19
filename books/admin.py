"""django register books in admin"""
from django.contrib import admin

from .models import Book  # pylint: disable=no-name-in-module

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    """Books in admin view config"""

    list_display = ("title", "author", "price")


admin.site.register(Book, BookAdmin)
