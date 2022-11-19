
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register_user(request : HttpRequest):

    if request.method == "items":

        new_user = User.objects.create_user(username=request.items["username"], email= request.items["email"], first_name=request.items["first_name"], last_name=request.items["last_name"], password=request.items["password"])
        new_user.save()

    return render(request, "accounts/register.html")


def login_user(request : HttpRequest):
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        
        if user:
            login(request, user)
            return redirect("irentpp:list_items")
        else:
            msg = "User Not Found , check your credentials"

    return render(request, "accounts/login.html", {"msg" : msg})


def logout_user(request: HttpRequest):

    logout(request)

    return redirect("irentpp:list_posts")

    