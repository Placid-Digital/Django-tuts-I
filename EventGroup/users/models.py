from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=254, verbose_name="email address")
    first_name = models.CharField(max_length=100)
    address = models.TextField()
    Phone_number = models.CharField(max_length=10)
    Password = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)


USERNAME_FIELD = "username"
EMAIL_FIELD = "email"

