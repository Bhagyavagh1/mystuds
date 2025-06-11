from django.db import models

# Create your models here.
class Student(models.Model):
    unm = models.CharField(max_length=40)
    prog = models.CharField(max_length=5)
    sec = models.CharField(max_length=1)
