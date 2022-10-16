from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    summary=models.TextField(max_length=2000)
    education= models.TextField(max_length=2000)
    experience=models.TextField(max_length=1000)
    project=models.TextField(max_length=1000)
    certificate=models.TextField(max_length=1000)
    career_objective=models.TextField(max_length=1000)
    skill=models.TextField(max_length=500,default="c")

    def __str__(self):
        return self.name
    

