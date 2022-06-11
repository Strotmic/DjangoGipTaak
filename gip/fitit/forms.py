from django import forms
from django.contrib.auth.models import User
from fitit.models import UserProfileInfo, Horloge


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ("profile_pic",)



class HorlogeForm(forms.ModelForm):
    class Meta:
        model = Horloge
        fields = ("model","merk","materiaal","prijs","horloge_pic")