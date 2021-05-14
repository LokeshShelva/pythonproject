from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
# Create your views here.


def login(response):
    return HttpResponse("<h1>Login works!</h1>")


def register(requests):
    if requests.method == 'POST':
        form = UserRegistrationForm(requests.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect("home")

    else:
        form = UserRegistrationForm()
    return render(requests, "user/register.html", {"form": form})
