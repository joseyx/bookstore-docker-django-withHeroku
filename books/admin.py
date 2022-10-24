"""django register books in admin"""
from django.contrib import admin

from .models import Book, Review, Images  # pylint: disable=no-name-in-module

# Register your models here.


class ReviewInLine(admin.TabularInline):
    """Reviews in admin view config"""

    model = Review


class ImagesInLine(admin.TabularInline):
    """Images in admin view config"""

    model = Images


class BookAdmin(admin.ModelAdmin):
    """Books in admin view config"""

    inlines = [
        ReviewInLine,
        ImagesInLine,
    ]

    list_display = ("title", "author", "price")


admin.site.register(Images)
admin.site.register(Book, BookAdmin)
