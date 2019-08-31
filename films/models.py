from django.db import models

# Create your models here.

class Film(models.Model):
    name = models.CharField()