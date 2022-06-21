from django.contrib import admin
from django.urls import path
from fitit import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


app_name = 'fitit'

urlpatterns = [
    path("register/", views.register, name="register"),
    path("user_login", views.user_login, name="user_login"),
    path("koop/<int:pk>/", views.koop, name="koop"),
    path("test", views.test, name="test"),
    path("aflos", views.aflos, name="aflos"),
    path("add_horloge", views.add, name="add_horloge"),
    path("horloges", views.horloges, name="horloges"),
    path("delete/<int:pk>/", views.HorlogeDelteView.as_view(), name="delete"),
]




