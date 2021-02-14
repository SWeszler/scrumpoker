from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=20, blank=False)
    vote = models.IntegerField(default=0)
    voted = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    def __repr__(self):
        return self.name
