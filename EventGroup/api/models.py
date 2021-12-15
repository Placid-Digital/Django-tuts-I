from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Users(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(_('email address'), unique=True)
    phone_no = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=250)
    # repeat_password = models.CharField(max_length=100)
    address = models.TextField

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username', 'first_name', 'phone_no', 'repeat_password','address','email' ]

    def __str__(self):
        return "{}".format(self.email)
