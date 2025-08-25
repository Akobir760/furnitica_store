from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        def __str__(self):
            return 'Custom user'