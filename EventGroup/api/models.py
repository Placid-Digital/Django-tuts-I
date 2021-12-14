from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    phone_no = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    repeat_password = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'phone_no', 'repeat_password']

    def __str__(self):
        return "{}".format(self.email)
