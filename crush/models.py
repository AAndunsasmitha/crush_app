from django.db import models

# Create your models here.

class Couples(models.Model):
    user_name = models.CharField(max_length=200)
    crush_name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)