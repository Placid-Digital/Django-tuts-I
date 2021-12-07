from django.db import models
# from django.contrib.auth.models import User


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Email_name =models.CharField(max_length=200)
    Password =models.CharField(max_length=500,blank=True,null=True)
    address = models.TextField()
    is_active=models.BooleanField(default=True)
