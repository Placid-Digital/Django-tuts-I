from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=100)
    contact =models.CharField(max_length=200)
    Email =models.CharField(max_length=200)
    Phone_number =models.CharField(max_length=100)
    Password =models.CharField(max_length=500,blank=True,null=True)
    address = models.TextField()
    is_active=models.BooleanField(default=True)

