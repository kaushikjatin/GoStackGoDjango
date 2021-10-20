from django.db import models


class Game_Score(models.Model):
    score = models.IntegerField()


def __str__(self):
    return self.score
