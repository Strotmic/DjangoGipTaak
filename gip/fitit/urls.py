from django.contrib import admin
from django.urls import path
from fitit import views
from django.conf.urls import include

app_name = 'fitit'

urlpatterns = [
    path("register/", views.register, name="register"),
    path("user_login", views.user_login, name="user_login"),
    path("koop", views.koop, name="koop"),
    path("aflos", views.aflos, name="aflos")
]
