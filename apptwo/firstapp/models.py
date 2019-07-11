from django.db import models

# Create your models here.

class user(models.Model):
    first_name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    email=models.EmailField(max_length=254,unique=True)
    user_name=models.CharField(max_length=128,unique=True)
    password=models.CharField(max_length=128)

class feedback(models.Model):
    name=models.CharField(max_length=128)
    course=models.CharField(max_length=128)
    topic=models.CharField(max_length=128)
    feedback=models.CharField(max_length=128)
