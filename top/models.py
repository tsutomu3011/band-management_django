from django.db import models


class Photo(models.Model):
    situation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.situation

class Wallet(models.Model):
    money = models.IntegerField()

    def __int__(self):
        return self.id