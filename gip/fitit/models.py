from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Horloge(models.Model):
    model = models.CharField(max_length=256)
    horloge_pic = models.ImageField(upload_to='horloge_pics', blank=True)
    materiaal = models.CharField(max_length=256)
    prijs = models.FloatField()
    merk = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse("fitit:horloges", kwargs={"pk": self.pk})

    def __str__(self):
        return self.merk



class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


# Create your models here.
