from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    marks=models.ImageField()
    amount=models.FloatField()
    email=models.EmailField()
