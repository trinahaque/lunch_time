from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def index(request):
    if 'first_name' in request.session:
        return redirect('/success')
    return render(request, "first_app/index.html")

def success(request):
    return render(request, "first_app/success.html")

def registration(request):
    if request.method == "POST":
        result = User.objects.registration(request)
        if result[0] == False:
            for error in result[1]:
                messages.add_message(request, messages.INFO, error)
        else:
            # messages.success(request, 'Registration successful')
            return redirect("/success")
    return redirect("/")


