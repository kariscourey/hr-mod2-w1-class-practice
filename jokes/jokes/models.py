from django.db import models

class Joke(models.Model):
    setup = models.TextField()
    punchline = models.TextField()
    laugh_count = models.PositiveSmallIntegerField(default=0)
