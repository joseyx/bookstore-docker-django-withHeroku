"""books forms"""
from django import forms

from .models import Review  # pylint: disable=no-name-in-module


class ReviewForm(forms.ModelForm):
    """form for creating a new review"""

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta"""

        model = Review
        fields = ("review",)
