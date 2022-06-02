from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
# Create your models here.
