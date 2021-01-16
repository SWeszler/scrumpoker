from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __repr__(self):
        return self.name
