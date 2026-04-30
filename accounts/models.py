from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Customers default to is_vendor=False; vendors set via admin or registration flag."""

    is_vendor = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
