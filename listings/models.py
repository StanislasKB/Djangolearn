from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#Create your models here.
class Tand(models.Model):                                                                           name = models.fields.CharField(max_length=100)




class Listing(models.Model):
    class Type(models.TextChoices):
        DISQUE = 'Records'
        AFFICHE = 'Posters'
        HABIT= 'Clothes'
        DIVERS = 'Miscellanous'

    types = models.fields.CharField(choices=Type.choices, max_length=100)


    title=models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=100)
    sold = models.fields.IntegerField()
    year = models.fields.IntegerField()


