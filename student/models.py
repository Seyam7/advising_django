from django.db import models

# Create your models here.

class addsub(models.Model):
    courseCode=models.CharField(max_length=40)
    email=models.CharField(max_length=40)