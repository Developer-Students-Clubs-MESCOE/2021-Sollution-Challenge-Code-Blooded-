from django.db import models

# Create your models here.
class Predictions(models.Model):
    date = models.CharField(max_length=64, primary_key=True)
    day = models.CharField(max_length=32)
    prediction = models.IntegerField()
