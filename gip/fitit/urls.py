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
    path("update/<int:pk>/", views.HorlogeUpdateView.as_view(), name="update"),
    path("updateUser/<int:pk>/", views.UpdateUser.as_view(), name="updateUser"),
    path("updatePhoto/<int:pk>/", views.updatePhoto, name="updatePhoto"),
    path("updatePassword/<int:pk>/", views.Password, name="updatePassword"),
    path("userprofile/<int:pk>/", views.UserDetails.as_view(), name="userprofile"),
]




