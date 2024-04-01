from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class RegistrationModel(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(auto_now=True)
   

    USERNAME_FIELD = 'email' 

    class Meta:
        db_table = "myregister"

class MyLonginModel(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=30)

    class Meta:
        db_table = "mylogin"
        