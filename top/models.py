from django.db import models

# Create your models here.
class Photo(models.Model):
  situation = models.CharField(max_length=200)
  image = models.ImageField(upload_to='images/')