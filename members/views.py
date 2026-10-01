from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Profile


def register(request):
    error = None
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            error = "Username already taken."
        else:
            user = User.objects.create_user(username=username, password=password)
            Profile.objects.create(user=user)
            return redirect("login")
    return render(request, "register.html", {"error": error})


def login_view(request):
    error = None
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user and user.profile.approved == True:
            login(request, user)
            return redirect("home")
        error = "Not approved yet."
    return render(request, "login.html", {"error": error})


@login_required
def home(request):
    return render(request, "home.html")


def logout_view(request):
    logout(request)
    return redirect("login")