from django.db import models
from django.contrib.auth.models import User

class UserRegistration(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Other')
    )

    uname = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES) 
    phone = models.CharField(max_length=20)
    newpassword = models.CharField(max_length=128)  
    confirmpassword = models.CharField(max_length=128)  

    def save(self, *args, **kwargs):
       
        if self.newpassword != self.confirmpassword:
            raise ValueError("Password and Confirm Password do not match")
        super().save(*args, **kwargs)

class LonginModel(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length =100)
    