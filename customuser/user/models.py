from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(("email address"), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "phone"]

    spouse_name = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email
