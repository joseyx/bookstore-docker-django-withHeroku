# pylint: disable=invalid-name
"""django import"""
# Generated by Django 4.1.2 on 2022-10-21 00:00

from django.db import migrations


class Migration(migrations.Migration):
    """migrations"""

    dependencies = [
        ("books", "0004_book_images"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="images",
        ),
    ]
