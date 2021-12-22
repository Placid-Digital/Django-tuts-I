from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Users(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(_('email address'), unique=True)
    phone_no = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=250)
    address = models.TextField(null=True, blank=True)

    # token = models.CharField(max_length=500, null=True, default="")

    def __str__(self):
        return "{}".format(self.email)


class Event(models.Model):
    mehadi = models.CharField(max_length=150)
    makeup = models.CharField(max_length=200)
    decoration = models.CharField(max_length=100)
    photography = models.CharField(max_length=250)
    catering = models.CharField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.email)
