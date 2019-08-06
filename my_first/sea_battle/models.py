from django.db import models
from datetime import datetime


# Create your models here.


class Player(models.Model):
    username = models.CharField(max_length=30)
    games = models.IntegerField(default=0)
    won_games = models.IntegerField(default=0)
    registration_date = models.DateTimeField()
    last_connection_date = models.DateTimeField()
    percent_of_victory = models.IntegerField(default=0)


class LastSession(models.Model):
    username = models.CharField(max_length=30)
