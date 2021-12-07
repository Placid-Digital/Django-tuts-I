from django.db import models

# Create your models here.

class Species(models.Model):
   name = models.CharField(max_length=100)
   classification = models.CharField(max_length=100)
   language = models.CharField(max_length=100)


class Person(models.Model):
   first_name = models.CharField(max_length=10)
   Email = models.CharField(max_length=10)
   Password = models.ForeignKey(Species, on_delete=models.DO_NOTHING)



