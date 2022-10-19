"""books models"""
import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    """books model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):  # pylint: disable=invalid-str-returned
        return self.title

    def get_absolute_url(self):
        """Return absolute url for the given book"""
        return reverse("book_detail", args=[str(self.id)])  # pylint: disable=no-member
