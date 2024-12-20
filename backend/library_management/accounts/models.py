from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('borrower', 'Borrower'),
    ]
    type = models.CharField(max_length=10, choices=USER_TYPES, default='borrower')

    # Optional: remove default fields
    is_superuser = models.BooleanField(default=False, blank=True, null=True)
    is_staff = models.BooleanField(default=False, blank=True, null=True)
