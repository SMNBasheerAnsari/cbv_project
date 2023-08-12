from django.db import models

# Create your models here.
class Triner(models.Model):
    triner_name=models.CharField(max_length=40,primary_key=True)
    subject=models.CharField(max_length=20)
    age=models.IntegerField()

