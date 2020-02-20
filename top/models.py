from django.db import models

class Photo(models.Model):
  situation = models.CharField(max_length=200)
  image = models.ImageField(upload_to='images/')
