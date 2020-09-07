from django.conf import settings
from django.db import models

class Account(models.Model):
    name = models.TextField()
    passhash = models.TextField()
    score = models.IntegerField()
    id = models.IntegerField(primary_key=True)


    def create(self):
        self.score = 0
        self.save()

    def __str__(self):
        return self.name

class Game(models.Model):
    game = models.TextField()
    img_url = models.TextField()
    totalplayers = models.IntegerField()
    function = models.IntegerField()
    id = models.IntegerField(primary_key=True)


    def add(self):
        self.save()

    def __str__(self):
        return self.game

class Team(models.Model):
    game_id = models.IntegerField(primary_key=True)
    team_players = models.IntegerField()
    team_names = models.TextField()


    def add(self):
        self.save()

    def __str__(self):
        return self.team_names
