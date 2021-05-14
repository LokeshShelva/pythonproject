from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def login(response):
    return HttpResponse("<h1>Login works!</h1>")


def register(response):
    form = UserCreationForm()
    return render(response, "user/register.html", {"form": form})
