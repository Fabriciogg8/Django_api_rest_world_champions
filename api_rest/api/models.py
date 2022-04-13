from django.db import models


# Create your models here.
class NationalTeam(models.Model):
    name = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)
    world_champion = models.PositiveIntegerField() 