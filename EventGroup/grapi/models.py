from django.db import models


# Create your models here.
class person(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(('email address'), unique=True)
    phone_no = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=250)
    address = models.TextField

    def __str__(self):
        return "{}".format(self.email)
