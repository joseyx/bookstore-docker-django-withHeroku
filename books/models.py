"""books models"""
import uuid
import os
from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.


def get_image_path(instance, filename):
    """get_image_path"""
    # pylint: disable=consider-using-f-string
    return os.path.join("images", "book_%s" % str(instance.title), filename)


class Book(models.Model):
    """books model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)

    def __str__(self):  # pylint: disable=invalid-str-returned
        return self.title

    def get_absolute_url(self):
        """Return absolute url for the given book"""
        return reverse("book_detail", args=[str(self.id)])  # pylint: disable=no-member


class Review(models.Model):
    """reviews model"""

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):  # pylint: disable=invalid-str-returned
        return self.review


class Images(models.Model):
    """images collection model"""

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(upload_to=get_image_path, blank=True)
