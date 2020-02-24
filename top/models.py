from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField


class Photo(models.Model):
    situation = models.CharField(max_length=200)
    image = cloudinary.models.CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return self.situation

class Wallet(models.Model):
    money = models.IntegerField()

    def __int__(self):
        return self.id