from django.db import models

class Curd(models.Model):

    name = models.CharField(max_length=50, unique=True)
    age = models.CharField(max_length=100)
    locotion= models.CharField(max_length=100)