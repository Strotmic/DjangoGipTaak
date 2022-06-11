from django.db import models
from django.contrib.auth.models import User



class Horloge(models.Model):
    model = models.CharField(max_length=256)
    horloge_pic = models.ImageField(upload_to='car_pics', blank=True)
    materiaal = models.CharField(max_length=256)
    prijs = models.FloatField()
    merk = models.CharField(max_length=256)

    def __str__(self):
        return self.merk


class UserProfileInfo(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


# Create your models here.
