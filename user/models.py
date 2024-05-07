from django.db import models

# Create your models here.

class student(models.Model):
    first_name=models.CharField(max_length=40)
    lastName=models.CharField(max_length=40)
    gender=models.CharField(max_length=20)
    p_email=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    password=models.CharField(max_length=15)