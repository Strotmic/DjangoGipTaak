from xml.dom.domreg import registered
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from fitit.forms import UserForm, UserProfileInfoForm, HorlogeForm
from fitit.aflosService import aflosService
from django.urls import reverse_lazy
from fitit.models import Horloge
from django.core.exceptions import SuspiciousOperation
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def horloges(request):
    list = Horloge.objects.order_by("prijs")
    print(str(list )+ " ok")
    return render(request, "fitit/horloges.html", {"list":list})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(f"{username} and {password}")
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("fitit:test"))
            else:
                return HttpResponse("Account is not active")
        else:
            print("Someone tried to login and failed")
            print(f"Username: {username} and password {password}")
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, "fitit/login.html", {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("fitit:test"))


@login_required
def special(request):
    return HttpResponse("you are logged in, nice")


def index(request):
    list = Horloge.objects.get()
    print(str(list )+ " ok")
    return render(request, "fitit/index.html", {"list":list})

def aflos(request):
    x = aflosService(3500,12,0.059)
    y = x.getTabel()
    return render(request, "fitit/aflos.html", {"y":y})

def koop(request, **kwargs):
    print(kwargs)
    list = Horloge.objects.order_by("prijs")
    for i in Horloge.objects.all():
        print(i)
    if request.method == "POST":
        tijd = request.POST['tijd']
        if int(tijd)<=1:
            return render(request, "fitit/koop.html")
        if int(tijd)>1 and int(tijd)<=6:
            rente = 0.10
        if int(tijd)>6 and int(tijd)<=12:
            rente = 0.085
        if int(tijd)>12 and int(tijd)<=24:
            rente = 0.065
        if int(tijd)>24:
            rente = 0.06
        x = aflosService(3500,int(tijd),rente)
        y = x.getTabel()
        return render(request, "fitit/aflos.html", {"y":y})
    else:
        return render(request, "fitit/koop.html")
    

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:

        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    return render(request, "fitit/registration.html", {"user_form": user_form, "profile_form": profile_form, "registered": registered})

def test(request):
    return render(request, "fitit/index2.html")

def add(request):
    if request.method == "POST":
        x = HorlogeForm(data=request.POST)

        if x.is_valid():
            horloge = x.save(commit=False)
        if "horloge_pic" in request.FILES:
            horloge.horloge_pic = request.FILES["horloge_pic"]

        horloge.save()
        registered = True
        return render(request, "fitit/index2.html")
    else: 
        x = HorlogeForm()
        return render(request, "fitit/add_horloge.html", {"x":x})


#def list(request)

class HorlogeUpdateView(UpdateView):
    fields = ("model","merk","materiaal","prijs","horloge_pic")
    model = Horloge

class HorlogeDelteView(DeleteView):
    model = Horloge
    success_url = reverse_lazy("fitit:horloges")
    