

# Create your models here.
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password =models.CharField(max_length=50)

class Marks(models.Model):
    sports=models.CharField( max_length=2,default='SOME STRING')
    artscraft=models.CharField( max_length=2,default='SOME STRING')
    singing=models.CharField( max_length=2,default='SOME STRING')
    acting=models.CharField( max_length=2,default='SOME STRING')
    readingbooks=models.CharField( max_length=2,default='SOME STRING')
    dancing=models.CharField( max_length=2,default='SOME STRING')
    other=models.CharField( max_length=2,default='SOME STRING')

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    def __str__(self):
       return self.name
