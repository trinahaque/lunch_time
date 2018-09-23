from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def index(request):
    # get all the users
    users = User.objects.all()
    print "users", users
    context = {
        "users": users
    }
    return render(request, "first_app/index.html", context)

def success(request):
    return render(request, "first_app/success.html")

def registration(request):
    if request.method == "POST":
        result = User.objects.registration(request)
        if result[0] == False:
            for error in result[1]:
                messages.add_message(request, messages.INFO, error)
        else:
            context = {
                "user": result[1]
            }
            return render(request, "first_app/success.html", context)
    return redirect("/")


