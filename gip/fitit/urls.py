from django.contrib import admin
from django.urls import path
from fitit import views
from django.conf.urls import url, include

app_name = 'fitit'

urlpatterns = [
    url(r"^register/$", views.register, name="register"),
    path("user_login", views.user_login, name="user_login")
]
