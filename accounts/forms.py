"""Accountos Forms"""
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form"""

    class Meta:  # pylint: disable=too-few-public-methods
        """meta class for custom user creation"""

        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    """Custom user change form"""

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta class for custom user change"""

        model = get_user_model()
        fields = (
            "email",
            "username",
        )
