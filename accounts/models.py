"""Django"""
# from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Custom user"""

    pass  # pylint: disable=unnecessary-pass
