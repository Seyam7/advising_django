from django.db import models

# Create your models here.

class admin(models.Model):
    email=models.CharField(max_length=40)
    adpass=models.CharField(max_length=40)

class addcourse(models.Model):
    courseName=models.CharField(max_length=40)
    courseCode=models.CharField(max_length=40)
    credit=models.FloatField()

class msg(models.Model):
    message=models.CharField(max_length=40)
    